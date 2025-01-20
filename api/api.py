import time

from flask import Flask # Flask turns python map into JSON line 9

app = Flask(__name__)

@app.route('/time') # a new route is being added (localhost/time to call it)
def get_current_time():
    return {'time' : time.time()} #JSON is a type of data representation protocol
#for simplicity

@app.route('/hello')
def say_hellow():
    return {'response' : 'hello world'}

#entry point for backhand