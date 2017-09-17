from flask import Flask, flash, session, render_template, redirect, request
import re

app= Flask(__name__)
app.secret_key = "fadskfm"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def hijk():

    return render_template("index.html")

@app.route('/check', methods=['POST'])
def lmnop():
    email=request.form['email']
    first_name=str(request.form['first_name'])
    last_name=str(request.form['last_name'])
    password=request.form['password']
    confirm_password=request.form['confirm_password']
    # li=[email,first_name,last_name,password,confirm_password]
    count=False

    if len(first_name)==0:
        flash('First name must be entered')
        count=True
    elif not str.isalpha(first_name):
        flash('Invalid first name')
        count=True
    if len(last_name)==0:
        flash('Last name must be entered')
        count=True
    elif not str.isalpha(last_name):
        flash('Invalid last name')
        count=True
    if len(password)==0:
        flash('Password must be entered')
        count=True
    elif len(password)<=8:
        flash('Password must be longer than 8 characters')
        count=True
    if len(confirm_password)==0:
        flash('Password confirmation must be entered')
        count=True
    elif confirm_password!=password:
        flash('Password and password confirmation did not match')
        count=True
    if len(email)==0:
        flash('Email must be entered')
        count=True
    elif not EMAIL_REGEX.match(email):
        flash('Not a valid email')
        count=True


    if count==False:
        flash('Success!')

    return redirect('/')



app.run(debug=True)