from flask import Flask, redirect, render_template, url_for, request

from database import db_session, init_db
from models import User
from internal_api import *

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


@app.route('/users/new', methods=['POST','GET'])
def users_new():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        new_user = User(name=str(username), email=str(email))
        db_session.add(new_user)
        db_session.commit()
    else:
        users = User.query.all()
        return render_template('users.html', users=users)

@app.route('api/scrape', methods=['POST'])
def scrape():
    if request.method == 'POST':
        url = request.form.get('url')
        pass


# classification functionality routes
#####################################

# classify all entities in the text and return as a dictionary
@app.route('/api/classify/all', methods=['POST', 'GET'])
def classify_all(req_url):
    return api_classify_all(api_scrape(req_url))

# classity a single entity and return a single integer representing the classification
@app.route('/api/classify/entity/<named_entity>', methods=['POST', 'GET'])
def classify_entity(req_url, named_entity):
    return api_classify_entity(api_scrape(req_url), named_entity)


@app.route('/api/classify/<req_url>/top/<int:j>')
def classify_top_j(req_url, j):
    return api_classify_top_j(api_scrape(req_url), j)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    return


if __name__ == '__main__':
    app.run()
