from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

class Party(db.Model):
    __tablename__ = 'parties'

    party_id = db.Column(db.Integer, primary_key=True)
    party_name = db.Column(db.String())

    def __init__(self, party_name):
        self.party_name = party_name
    
    def serialize(self):
        return {
            'party_id': self.party_id, 
            'party_name': self.party_name
        }

class Quotation(db.Model):
    __tablename__ = 'quotations'

    quotation_id = db.Column(db.Integer, primary_key=True)
    quotation = db.Column(db.String())
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id')) # Party from whose manifesto the quotation was taken
    party = db.relationship("Party")

    def __init__(self, quotation, party_id):
        self.quotation = quotation
        self.party_id = party_id
    
    def serialize(self):
        return {
            'quotation_id': self.quotation_id,
            'quotation': self.quotation,
            'party_id': self.party_id
        }     

class Session(db.Model):
    __tablename__ = 'sessions'

    session_id = db.Column(UUID(as_uuid=True), primary_key=True)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id')) # This may be null if the session player does not give a party affiliation
    party = db.relationship("Party")

    def __init__(self, session_id, party_id):
        self.session_id = session_id
        self.party_id = party_id

    def serialize(self):
        return {
            'session_id': self.session_id, 
            'party_id': self.party_id
        }

class Answer(db.Model):
    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, primary_key=True)
    quotation_id = db.Column(db.Integer, db.ForeignKey('quotations.quotation_id')) # id of quotation shown to user
    quotation = db.relationship("Quotation")
    session_id = db.Column(UUID(as_uuid=True), db.ForeignKey('sessions.session_id')) # quiz session id  
    session = db.relationship("Session")
    party_id_guess = db.Column(db.Integer, db.ForeignKey('parties.party_id')) # id of the party the user has responded with
    party = db.relationship("Party")
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, quotation_id, session_id, party_id_guess):
        self.quotation_id = quotation_id
        self.session_id = session_id
        self.party_id_guess = party_id_guess
    
    def serialize(self):
        return {
            'answer_id': self.answer_id,
            'quotation_id': self.quotation_id, 
            'session_id': self.session_id, 
            'party_id_guess': self.party_id_guess,
            'created_at': self.created_at
        }
