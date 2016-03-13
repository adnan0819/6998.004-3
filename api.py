from flask import Flask, request
from flask.ext.cors import CORS
import json
import calculations

# This script is to create the API based on the records in Redis. Note that I have 
# stored the deltas in db=0 and the distributions in db=1


app = Flask(__name__) # thanks to PROF. DEWAR, THIS TOOL TOOK CARE OF CORS ISSUE which he helped me via email. 
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/probability')
def get_probability():
    msg = request.args.get('tag') #this is the implementation of the GET request using the API
    prob = calculations.probability(msg)
    response = { 'tag': msg, 'p': prob }
    return json.dumps(response)

@app.route('/rate')
def get_rate():
    rate = calculations.rate()
    return json.dumps( {'rate for now ': rate})


@app.route('/histogram')
def get_histogram():
    hist = calculations.histogram()
    return json.dumps(hist)


@app.route('/entropy')
def get_entropy():
    entropy = calculations.entropy()
    return json.dumps({'entropy': entropy})



if __name__ == '__main__':
    app.run(debug=True)