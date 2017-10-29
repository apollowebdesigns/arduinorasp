from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import datetime
import time
from time import sleep
from flask_cors import CORS, cross_origin
import forwards
app = Flask(__name__)
CORS(app)

@app.route('/forwards', methods=['GET'])
def move_forwards():
    return forwards.move()

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True)