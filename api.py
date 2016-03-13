# api.py
# Jonah Smith
# Assignment 3, Storytelling with Streaming Data, Spring 2016
#
# This script connects to a Redis database (table 0 with time diffs between
# events, table 1 with a distribution over articles), and defines an API to
# access certain calculations, including the rate, the histogram, the entropy,
# and the probability of a given message.

from flask import Flask, request
from flask.ext.cors import CORS
import json
import calculations

app = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/rate')
def get_rate():
    rate = calculations.rate()
    return json.dumps( {'avg_rate': rate})


@app.route('/histogram')
def get_histogram():
    hist = calculations.histogram()
    return json.dumps(hist)


@app.route('/entropy')
def get_entropy():
    entropy = calculations.entropy()
    return json.dumps({'entropy': entropy})


@app.route('/probability')
def get_probability():
    msg = request.args.get('message')
    prob = calculations.probability(msg)
    response = { 'message': msg, 'p': prob }
    return json.dumps(response)




if __name__ == '__main__':
    app.run(debug=True)