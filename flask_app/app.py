from flask import Flask

from internal_api import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# scraping functionality route
@app.route('/api/scrape/<req_url>')
def scrape(req_url):
    return api_scrape(req_url)


# classification functionality routes
#####################################

# classify all entities in the text and return as a dictionary
@app.route('/api/classify/<req_url>')
def classify_all(req_url):
    return api_classify_all(api_scrape(req_url))


# classity a single entity and return a single integer representing the classification
@app.route('/api/classify/<req_url>/entity/<named_entity>')
def classify_entity(req_url, named_entity):
    return api_classify_entity(api_scrape(req_url), named_entity)


@app.route('/api/classify/<req_url>/top/<int:j>')
def classify_top_j(req_url, j):
    return api_classify_top_j(api_scrape(req_url), j)


if __name__ == '__main__':
    app.run()
