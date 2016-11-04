from hashlib import md5
from flask import render_template,request,redirect,url_for,flash,session

def auth(username,password):
  if username == "123":
    session['username'] = '123'
    return True
  else:
    return False

def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    print(url_for('index'))
    if auth(username,password):
      return redirect(url_for('index'))
    else:
      flash('Invalid username')
      return redirect(url_for('login'))
  else:
    return render_template('login.html')

def logout():
  session.pop('username',None)
  return redirect(url_for('login'))

def is_login():
  return True
