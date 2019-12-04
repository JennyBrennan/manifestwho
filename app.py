from flask import Flask, request, jsonify, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update
import logging
import os
import uuid

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

def get_parties():
    from models import Party
    try: 
        parties=Party.query.all()
        return  parties
    except Exception as e:
	    return render_template("error.html", error=str(e))

def add_session(session_id):
    from models import Session
    try: 
        quiz_session=Session(
            session_id=session_id,
            party_id=None
        )
        db.session.add(quiz_session)
        db.session.commit()
        return "Session added. Session id={}".format(quiz_session.session_id)
    except Exception as e:
        db.session.rollback()
        return render_template("error.html", error=str(e))

def get_quotation(session_id):
    from models import Quotation, Answer
    try:
        query=db.session.query(Answer.quotation_id).filter(Answer.session_id == session_id)
        quotation=db.session.query(Quotation).filter(Quotation.election == 'GE 2019').filter(Quotation.quotation_id.notin_(query)).order_by(func.random()).first() # Get random quotation
        return quotation
    except Exception as e:
        return render_template("error.html", error=str(e))

def get_quotations_answered(session_id):
    from models import Quotation, Answer
    try:

        answers=db.session.query(Answer, Quotation).\
            join(Quotation, Quotation.quotation_id==Answer.quotation_id).\
            filter(Answer.session_id == session_id).\
            filter(Quotation.election == 'GE 2019').all()
        return answers
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.route("/answer", methods=['GET','POST'])
def add_answer():
    quotation_limit = 8
    parties=get_parties()

    if request.cookies.get('manifestwho') is not None:
        cookie=request.cookies.get('manifestwho')
        session_id=uuid.UUID(cookie)
    else:
        session_id=uuid.uuid4()
        add_session(session_id)

    if request.method == 'POST':
        from models import Answer
        quotation_id=request.form.get('quotation_id')
        party_id_guess=request.form.get('party')
        try:
            answer=Answer(
                session_id=session_id,
                quotation_id=quotation_id,
                party_id_guess=party_id_guess
            )
            db.session.add(answer)
            db.session.commit()
        except Exception as e:
            return render_template("error.html", error=str(e))

    quotations_answered=get_quotations_answered(session_id)
    quotation_row=get_quotation(session_id)

    if len(quotations_answered) >= quotation_limit:
        response = make_response(redirect(url_for('affiliation')))
    else: 
        response = make_response(render_template("question.html", quotation=quotation_row, parties=parties))

    response.set_cookie('manifestwho', value=str(session_id))

    return response


@app.route("/affiliation", methods=['GET','POST'])
def affiliation():
    if request.method == 'POST':
        from models import Session
        cookie=request.cookies.get('manifestwho')
        session_id=uuid.UUID(cookie)
        party_id=request.form.get('party_affiliation')
        try:
            session_to_update=db.session.query(Session).filter(Session.session_id == session_id).first()
            session_to_update.party_id=party_id
            db.session.commit()
            return redirect(url_for('results'))
        except Exception as e:
            return(str(e))
    parties=get_parties()
    return render_template("affiliation.html", parties=parties)
    

@app.route("/results")
def results():
    from models import Answer, Quotation, Party
    cookie=request.cookies.get('manifestwho')
    session_id=uuid.UUID(cookie)

    try: 
        guess = db.aliased(Party)
        correct = db.aliased(Party)
        new_data=db.session.query(Answer, Quotation, guess.party_name, correct.party_name).\
            join(Quotation, Quotation.quotation_id==Answer.quotation_id).\
            join(guess, guess.party_id == Answer.party_id_guess).\
            join(correct, correct.party_id == Quotation.party_id).\
            filter(Answer.session_id == session_id).\
            filter(Quotation.election == 'GE 2019').all()
        
        answers_given_count=len(new_data)
        
        correct_answers_count=0
        for d in new_data:
            if d.Quotation.party_id == d.Answer.party_id_guess:
                correct_answers_count+=1

        return render_template("results.html", correct_count=correct_answers_count, total_answers=answers_given_count, results=new_data)
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.route("/reset")
def reset():
    response=make_response(redirect(url_for('homepage')))
    response.set_cookie('manifestwho', '', expires=0)
    return response

if __name__ == '__main__':
    app.run()