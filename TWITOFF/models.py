from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

class User (DB.Model):
    """ Twitter users that we analyze """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15))
    newest_tweet_id = DB.column(DB.BigInteger) 
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet (DB.Model):
    """Tweets we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.column(DB.BigInteger, DB.ForeignKey('user.id'))
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    def __repr__(self):
        return 'Tweet {}>'.format(self.text)
    