from flask import Flask, redirect, render_template, url_for

from database import db_session, init_db
from models import User

app = Flask(__name__)
init_db()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/users/new/<username>/<email>')
def user_new(username, email):
    new_user = User(name=str(username), email=str(email))
    db_session.add(new_user)
    db_session.commit()
    return redirect(url_for('user_index'))


@app.route('/users')
def user_index():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    return


if __name__ == '__main__':
    app.run()
