from flask import Flask,render_template
from settings import setting
from view import auth


app = Flask(__name__)

@app.route('/')
@auth.is_login
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
  return auth.login()

@app.route('/logout')
def logout():
  return auth.logout()

@app.route('/<userid>')
def getUserAll(userid):
  pass

@app.route('/<objectid>')
def object(objectid):
  pass

@app.route('/filter')
def filter():
  pass


if __name__ == "__main__":
  app.secret_key = setting['secret_key']
  app.run(debug=setting['debug'])
