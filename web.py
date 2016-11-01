from flask import Flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  pass

@app.route('/login')
def login():
  pass

@app.route('/logout')
def logout():
  pass

@app.route('/<userid>')
def getUserAll():
  pass

@app.route('/<objectid>')
def object():
  pass

@app.route('/filter')
def filter():
  pass
