Take Home Code Test
===================

Implement a REST service using a python web framework such as flask or django that can be used to store, fetch, and update user records. A user record can be represented in a JSON hash like so:

```json
{
    "first_name": "Joe",
    "last_name": "Smith",
    "userid": "jsmith",
    "groups": ["admins", "users"]
}
```


The service should provide the following endpoints and semantics:

```
GET /users/<userid>
    Returns the matching user record or 404 if none exist.
```

```
POST /users
    Creates a new user record. The body of the request should be a valid user
    record. POSTs to an existing user should be treated as errors and flagged
    with the appropriate HTTP status code.
```

```
DELETE /users/<userid>
    Deletes a user record. Returns 404 if the user doesn't exist.
```

```
PUT /users/<userid>
    Updates an existing user record. The body of the request should be a valid
    user record. PUTs to a non-existant user should return a 404.
```

```
GET /groups/<group name>
    Returns a JSON list of userids containing the members of that group. Should
    return a 404 if the group doesn't exist.
```

```
POST /groups
    Creates a empty group. POSTs to an existing group should be treated as
    errors and flagged with the appropriate HTTP status code. The body should contain
    a `name` parameter
```

```
PUT /groups/<group name>
    Updates the membership list for the group. The body of the request should 
    be a JSON list describing the group's members.
```

```
DELETE /groups/<group name>
    Deletes a group.
```

Implementation Notes:

1. Any design decisions not specified herein are fair game. Completed
projects will be evaluated on how closely they follow the spec, their
design, and cleanliness of implementation.

2. Completed projects must include a README with enough instructions
for evaluators to build and run the code. Bonus points for builds
which require minimal manual steps.

3. Remember this project should take a maximum of 8 hours to
complete. Do not get hung up on scaling or persistence issues. This is
a project used to evaluate your design and implementation skills only.

4. Please include any unit or integration tests used to verify
correctness.

# Heroku Python Skeleton

This repository has all the base files ready for deploying a Heroku
application, including a simple database model managed with
flask-sqlalchemy.

## Usage
https://daily-planet.herokuapp.com/ | https://git.heroku.com/daily-planet.git

Creating postgresql-triangular-9570... done, (free)
Adding postgresql-triangular-9570 to daily-planet... done
Setting DATABASE_URL and restarting daily-planet... done, v4
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pgbackups:restore
Use `heroku addons:docs heroku-postgresql` to view documentation.

### Initial

```bash
$ git clone https://github.com/yuvadm/heroku-python-skeleton.git
$ cd heroku-python-skeleton
$ heroku create
$ git push heroku master
```

### Database

```bash
$ heroku addons:add heroku-postgresql:dev
-----> Adding heroku-postgresql:dev to some-app-name... done, v196 (free)
Attached as HEROKU_POSTGRESQL_COLOR
Database has been created and is available
$ heroku pg:promote HEROKU_POSTGRESQL_COLOR
$ heroku run python
```

and in the Python REPL:

```python
>>> from app import db
>>> db.create_all()
```

For a detailed introduction see [http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/](http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/).
