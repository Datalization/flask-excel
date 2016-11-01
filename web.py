from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('login.html')

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

if __name__ == "__main__":
  # app = create_app(config="config.yaml")
  # app.run(use_debugger=use_debugger, debug=app.debug,use_reloader=use_debugger, host='0.0.0.0')
  app.run()
