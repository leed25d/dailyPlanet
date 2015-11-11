import os
import dumper
import logging

from flask import Flask, jsonify, request, abort
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, joinedload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.reflect()
def try_commit():
    try:
        db.session.commit()
        return True
    except Exception, e:
        logging.warn( "try_commit() Exception during commit '%s'" % (str(e)))
        return False

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

@app.errorhandler(400)
def bad_request(error=None):
    message = {
            'status': 400,
            'message': 'Bad Request: ' + str(request.json),
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.errorhandler(500)
def server_error(error=None):
    message = {
            'status': 500,
            'message': 'Server Error: ' + str(request)
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp

########################################################################
##  GET /users/<userid>
##      Returns the matching user record or 404 if none exist.
##----
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

########################################################################
##  POST /users
##      Creates a new user record. The body of the request should be a valid user
##      record. POSTs to an existing user should be treated as errors and flagged
##      with the appropriate HTTP status code.
##----
@app.route('/users', methods=['POST'])
def create_user():
    ##logging.warn( "create_user() entered")
    if not request.json or not 'userid' in request.json:
        logging.error( "create_user() userid is missing")
        return bad_request()

    user = Users()
    for key in ('userid', 'last_name', 'first_name'):
        user.__dict__[key]= request.json.get(key, None)
    db.session.add(user)

    if not try_commit():
        logging.error( "create_user() commit failed")
        server_error(500)

    retcode= dict([('message','user %s created' % (request.json['userid']))])
    return(users_get(request.json['userid']), 201)

########################################################################
##  DELETE /users/<userid>
##      Deletes a user record. Returns 404 if the user doesn't exist.
##----
@app.route('/users/<uid>', methods=['DELETE'])
def delete_user(uid):
    ##logging.warn( "delete_user() entered")
    q= Users.query.filter(Users.userid == str(uid).lower())
    if (q.count() == 0):
        return not_found()
    if (q.count() != 1):
        return server_error()

    db.session.delete(q.first())
    if not try_commit():
        logging.error( "delete_user() commit failed")
        server_error(500)

    retcode= dict([('message','user %s deleted' % (uid))])
    return(jsonify(retcode), 200)

########################################################################
##  PUT /users/<userid>
##      Updates an existing user record. The body of the request should be a valid
##      user record. PUTs to a non-existant user should return a 404.
##----
@app.route('/users/<uid>', methods=['PUT'])
def update_user(uid):
    logging.warn( "update_user() entered.  uid= %s" % (uid))
    if not request.json:
        logging.error( "update_user() no parameter block found")
        return bad_request()

    q= Users.query.filter(Users.userid == str(uid).lower())
    if (q.count() == 0):
        return not_found()
    if (q.count() != 1):
        logging.error( "update_user() q.count()= %d" % (q.count()))
        return server_error()

    usr= q.first()
    for key in ('last_name', 'first_name', 'userid'):
        usr.__setattr__(key, request.json.get(key, usr.__dict__[key]))

    if not try_commit():
        logging.error( "update_user() commit failed")
        server_error(500)
        
    return(users_get(usr.userid), 200)

########################################################################
##  GET /groups/<group name>
##      Returns a JSON list of userids containing the members of that group. Should
##      return a 404 if the group doesn't exist.
##----
@app.route('/groups/<group_name>', methods=['GET'])
def get_group(group_name):
    logging.error( "get_group() entry")
    server_error(500)
########################################################################
##  POST /groups
##      Creates a empty group. POSTs to an existing group should be treated as
##      errors and flagged with the appropriate HTTP status code. The body should contain
##      a `name` parameter
##----
@app.route('/groups', methods=['POST'])
def create_group():
    server_error(500)
########################################################################
##  PUT /groups/<group name>
##      Updates the membership list for the group. The body of the request should 
##      be a JSON list describing the group's members.
##----
@app.route('/groups/<group_name>', methods=['PUT'])
def edit_group(group_name):
    server_error(500)
########################################################################
##  DELETE /groups/<group name>
##      Deletes a group.
##----
@app.route('/groups/<group_name>', methods=['DELETE'])
def delete_group(group_name):
    server_error(500)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
