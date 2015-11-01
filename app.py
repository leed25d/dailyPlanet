import os
import dumper

from flask import Flask, jsonify, request
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, joinedload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.reflect()

class UsersGroups(db.Model):
    __tablename__ = 'users_groups'
    group = relationship("Groups", backref="users_assocs", lazy='joined')

class Users(db.Model):
    __tablename__ = 'users'
    groups = relationship("UsersGroups", backref="users", lazy='joined')

class Groups(db.Model):
    __tablename__ = 'groups'


@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/users/<uid>', methods=['GET'])
def users_get(uid):
    q= Users.query.filter(Users.userid == str(uid).lower())
    if (q.count() == 0):
        return not_found()

    usr= q.first()
    attrs= ('first_name','last_name','userid')
    retcode= dict((key, str(usr.__dict__.get(key, None))) for key in attrs)
    retcode['groups'] = [entry.group.name for entry in usr.groups ]
    return(jsonify(retcode))



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
