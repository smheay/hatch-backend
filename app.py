from flask import Flask, request, jsonify, make_response, redirect

from model_json import model
from tests_model import test_model

#import multiprocessing 

app = Flask(__name__)

@app.route("/")
def hello_world():

    if app.debug:
        test_model.test_ping_request()
        test_model.test_get_posts_api()
    
    return f"Hello World!  {app.debug}", 200



@app.route('/<page_name>')
def not_made(page_name):
    return redirect( "/")

  
@app.route("/assessment/blog/posts/", methods=['GET'])
def index():
    #Get the string param and store in tag  (i.e. ?tags=some-value)
    args = request.args
    tags = args.get('tags')
    entries = model.get_request(tags)
    return jsonify(entries)



@app.route('/api/ping')
def ping_request():
    entries = model.ping_request()
    return jsonify(entries), 204



@app.route("/api/posts/")  
def get_posts_api():  
    args = request.args

    tag = args.get('tags')
    sort_by = args.get('sortBy')
    direction = args.get('direction')

    entries = model.get_posts_api(tag, sort_by, direction)
    keys = list(entries.keys())

    if tag == '':
        return jsonify(entries), 400

    if keys[0] == 'error':
        return jsonify(entries), 400

    else: 
        return jsonify(entries), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0')