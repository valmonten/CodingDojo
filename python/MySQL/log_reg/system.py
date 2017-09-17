from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'friendly')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forming', methods=['POST'])
def input():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    email=request.form['email']
    password=request.form['password']
    conf=request.form['confirmation']
    
    check = True
    if len(first_name)<2:
        flash('First name must be at least 2 letters')
        check= False
    elif not str.isalpha(first_name):
        flash('Names can only contain letters')
        check= False
    if len(last_name)<2:
        flash('Last name must be at least 2 letters')
        check= False
    elif not str.isalpha(last_name):
        flash('Names can only contain letters')
        check= False
    if not EMAIL_REGEX.match(email):
        flash('Invalid email')
        check= False
    if len(password)<8:
        flash('Password must be at least 8 characters long')
        check= False
    if password!=conf:
        flash('Passwords do not match')
        check= False
    
    if check ==True:
        flash('Success!')
        query="INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (:first_name,:last_name,:email,:password,NOW(),NOW())"
        data={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }
    
    

    

app.run(debug=True)