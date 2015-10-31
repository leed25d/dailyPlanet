# Heroku Python Skeleton

This repository has all the base files ready for deploying a Heroku application, including a simple database model managed with flask-sqlalchemy.

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
