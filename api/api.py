import time

from flask import Flask, request # Flask turns python map into JSON line 9
from legoapi.query import LegoQuery

app = Flask(__name__, static_folder='../build', static_url_path='/') # HTML UI

@app.route('/api/time') # a new route is being added (localhost/time to call it)
def get_current_time():
    return {'time' : time.time()} #JSON is a type of data representation protocol
#for simplicity

@app.route('/api/hello')
def say_hellow():
    return {'response' : 'hello world'}

@app.route('/')
def index():
    return app.send_static_file('index.html')

#entry point for backhand

@app.route('/api/search')
def search():
    #app.logger.info(request.form)
   
    keyword = "pig" #equest.form["keyword"]
    legoquery = LegoQuery('lego.com')
    response = legoquery.search(keyword)
    return response
