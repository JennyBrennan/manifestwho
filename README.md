# ManifestWho?

A game of guessing UK political party manifestos: [manifestwho.com](https://manifestwho.com).

Manifestwho is a quiz about UK political manifestos. It's mainly supposed to be fun (for a niche, political kind of fun). It's also a little experiment into how well people can recognise messages from manifestos - we've got a suspicion it's quite hard.

Built in Python using Flask and a Postgres database. Deployed on Heroku at manifestwho.com. Contributions are very welcome (more details below). 

## General Election 2019 Manifesto reference

General Election 2019 manifestos used to source quotations, in alphabetical order (last accessed 1st Dec):

- [Brexit Party](https://www.thebrexitparty.org/wp-content/uploads/2019/11/Contract-With-The-People.pdf)
- [Conservative Party](https://assets-global.website-files.com/5da42e2cae7ebd3f8bde353c/5dda924905da587992a064ba_Conservative%202019%20Manifesto.pdf)
- [Green Party](https://www.greenparty.org.uk/assets/files/Elections/Green%20Party%20Manifesto%202019.pdf)
- [Labour Party](https://labour.org.uk/wp-content/uploads/2019/11/Real-Change-Labour-Manifesto-2019.pdf)
- [Liberal Democrats](https://d3n8a8pro7vhmx.cloudfront.net/libdems/pages/57307/attachments/original/1574876236/Stop_Brexit_and_Build_a_Brighter_Future.pdf?1574876236)

Read more about manifesto inclusion choices in the [FAQ](https://manifestwho.com/faq).

## Contributing to ManifestWho?

If you'd like to make a change or improvement via GitHub, you can fork the repository and make a pull request using these steps:

1. Click 'fork' at the top of this repository
2. Clone down your fork using `git clone https://github.com/YOUR-USERNAME/manifestwho`
3. Create a new branch with the name of the meetup you're adding
4. Make your change 
5. Push your new branch and changes up to your fork of the repository
6. Go to your branch in your repository on GitHub, and click the green 'New pull request' button on the left (making sure the base fork is set to JennyBrennan/manifestwho)
7. If I've not got back to you about your PR in a resonable time, feel free to nudge me on Twitter [@jennyhbren](https://twitter.com/jennyhbren)


## Related reading

* [Create a web application with Python, Flask and PostgreSQL](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)
* [SQLAlchemy ORM tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

## Running locally

From within the manifestwho folder, start the virtual environment:

```
. venv/bin/activate
```

You'll need to set environment variables for ``APP_SETTINGS`` and ``DATABASE_URL``, either via the terminal or a .env file:

```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/manifestwho"
```

Run the app:

```
python3 app.py
```

## TODOs

A few things I'd like to tackle in the future:

* Allow people to go back and play previous versions (EU elections 2019 version).
* Automate testing - at the moment I'm manually testing the app as I chucked it up pretty quickly as a proof of concept; would be better to have tests that mock postgres and/or run end-to-end UI tests with Selenium or similar.
* Add web analytics to monitor where participants are based and where referrals are coming from (e.g. if all participants were in the US, then the data won't tell us much about UK public understanding).
* Consider additional voluntary data collection at the end e.g. voting intention. Look into the best ways of phrasing these from existing research.
* A sharing/social media plan to get the word out and increase participation.
* Design a swanky logo and add favicon.

There's also likely a bunch of general tidying/improvement that could be done in the code - I'm new to this stack (beyond teaching the [Code First Girls](https://codefirstgirls.org.uk) Python Course) and picked it as a quick learning opportunity, so suggestions welcome!
