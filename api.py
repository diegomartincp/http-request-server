from flask import Flask,jsonify
import flask

app = Flask(__name__)

#Cualquier ruta
@app.route("/")
def hello_world():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response