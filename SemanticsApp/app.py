from flask import Flask, redirect, render_template, url_for, request

from database import db_session, init_db
from models.User import User
from internal_api import *

app = Flask(__name__)
init_db()


@app.errorhandler(404)
def page_not_found():
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>/')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/users/new/<username>/<email>/')
def user_new(username, email):
    new_user = User(name=str(username), email=str(email))
    db_session.add(new_user)
    db_session.commit()
    return redirect(url_for('user_index'))


@app.route('/users/')
def user_index():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/new/', methods=['POST', 'GET'])
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


# Scraping and Classification
#####################################
# - Scraping
# - Classification


# Scraping 
#####################################
@app.route('/api/scrape/', methods=['POST', 'GET'])
def scrape():
    if request.method == 'POST':
        url = request.form.get('url')
        pass
    elif request.method == 'GET':
        pass
    else:
        pass


# Classifications
#####################################
# - All
# - Entity
# - Top-j

# Classify All Named Entities
#####################################
@app.route('/api/classify/all', methods=['POST,' 'GET'])
def classify_all(req_url):
    return api_classify_all(api_scrape(req_url))


# Single Entity Classification
#####################################
@app.route('/api/classify/entity/<named_entity>', methods=['GET'])
def classify_entity_get(req_url, named_entity):
    if request.method != 'GET':
        return page_not_found()
    return api_classify_entity(api_scrape(req_url), named_entity)


@app.route('/api/classify/entity/', methods=['POST'])
def classify_entity_post(req_url, named_entity):
    if request.method != 'POST':
        return page_not_found()
    return api_classify_entity(api_scrape(req_url), named_entity)


# Top-J Classification
#####################################
@app.route('/api/classify/<req_url>/top/<int:j>', methods=['GET'])
def classify_top_j_get(req_url, j):
    if request.method != 'GET':
        return page_not_found()
    return api_classify_top_j(api_scrape(req_url), j)


@app.route('/api/classify/top/', methods=['POST'])
def classify_top_j_post(req_url, j):
    if request.method != 'POST':
        return page_not_found()
    return api_classify_top_j(api_scrape(req_url), j)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    return


if __name__ == '__main__':
    app.run()
