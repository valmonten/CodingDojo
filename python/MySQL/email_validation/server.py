from flask import Flask, render_template, redirect, request, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email_valid')
app.secret_key= 'YUp'
@app.route('/')
def check():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def checking():
    email=request.form['email_address']
    if email:
        query= 'SELECT * FROM user WHERE email= :specific_email'
        data = {'specific_email': email}
        user = mysql.query_db(query,data)
        print email
        if user:
            if user[0]['email']==email:
                print "Valid"
                flash('Email already exists in database')
                return redirect('/')
        else:
            query2='INSERT INTO user (email, created_at, updated_at) VALUES(:email, NOW(), NOW())'
            data2 = {'email': email}
            mysql.query_db(query2, data2)
            users=mysql.query_db('SELECT * FROM user')
            print users
            return render_template('success.html', users=users)

        
    
# an example of running a query
# print mysql.query_db("SELECT * FROM friends")
app.run(debug=True)
