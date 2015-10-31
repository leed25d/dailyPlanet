import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.reflect()

##  class User(db.Model):
##      id = db.Column(db.Integer, primary_key=True)
##      first_name = db.Column(db.String(80))
##      last_name = db.Column(db.String(80))
##      userid = db.Column(db.String(80))
##  
##      def __init__(self, first_name, last_name, userid):
##          self.first_name = first_name
##          self.last_name = last_name
##          self.userid = userid
##  
##      def __repr__(self):
##          return '<User %r>' % self.name
##  
##  class Group(db.Model):
##      id = db.Column(db.Integer, primary_key=True)
##      self.name = db.Column(db.String(80))
##  
##      def __init__(self, first_name, last_name, userid):
##          self.name = name
##  
##      def __repr__(self):
##          return '<Group %r>' % self.name


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
