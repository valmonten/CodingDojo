from flask import Flask, render_template, redirect, request, flash, session
# import the Connector function
from mysqlconnection import MySQLConnector
import re, md5, os, binascii
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'the_wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key= 'YUp'
@app.route('/')
def check():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def registration():
    salt = binascii.b2a_hex(os.urandom(15))

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']

    hashed_pw = md5.new(password + salt).hexdigest()

    valid = True
    
    if len(first_name)<2:
        flash('First name must be at least 2 letters')
        valid= False
    elif not str.isalpha(str(first_name)):
        flash('Names can only contain letters')
        valid= False
    if len(last_name)<2:
        flash('Last name must be at least 2 letters')
        valid= False
    elif not str.isalpha(str(last_name)):
        flash('Names can only contain letters')
        valid= False
    if not EMAIL_REGEX.match(email):
        flash('Invalid email')
        valid= False
    if len(password)<8:
        flash('Password must be at least 8 characters long')
        valid= False
    if password!=confirm:
        flash('Passwords do not match')
        valid= False


    query = "SELECT users.email FROM users"
    emailing = mysql.query_db(query)



    for em in emailing:
        print em['email']
        if em['email']==email:
            valid=False
            flash('That email already exists')


    if valid==True:
        flash('Success!')
        query = "INSERT INTO users (first_name,last_name,email,password, salt,created_at,updated_at) VALUES(:first_name,:last_name,:email,:password, :salt ,NOW(),NOW())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password':hashed_pw,
            'salt': salt
        }
        mysql.query_db(query,data)



    return redirect('/')

@app.route('/login', methods=['POST'])
def verify():
    email=request.form['email']
    password=request.form['password']
    # Match the email if it exists
    # Error if email does not exist
    # Check that email's password and see if it matches
    # Error if the password does not match
    # Create a session that confirms the log in
    # redirect to root if error, render_template if success
    query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    data = {'email': email}
    matching = mysql.query_db(query, data)
    # Adjust if statements for login
    if len(matching) !=0:
        encrypted_password = md5.new(password + matching[0]['salt']).hexdigest()
        if matching[0]['password'] == encrypted_password:
            session['first_name'] =matching[0]['first_name']
            session['id'] = matching[0]['id']
            return redirect('/wall')
        else:
            #Login error
            flash('Incorrect password')
            return redirect('/')
    else:
        flash('Email and password combination does not exist')
            


    return redirect('/')
@app.route('/wall')
def shows():
    query = 'SELECT messages.message, users.first_name, users.last_name, messages.id, messages.updated_at FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.updated_at DESC'
    info = mysql.query_db(query)
    query2 = 'SELECT * FROM users JOIN comments ON comments.user_id = users.id JOIN messages ON messages.id = comments.message_id ORDER BY comments.updated_at ASC'
    info2 = mysql.query_db(query2)



    return render_template('wall.html', first=session['first_name'], info=info, info2=info2)

@app.route('/logoff', methods=['POST'])
def logoff():
    session.clear()
    return redirect('/')
@app.route('/new_message', methods=['POST'])
def posting_message():
    message=request.form['message']
    
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
    data={
        'message':message,
        'user_id':session['id']
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/new_comment', methods=['POST'])
def posting_comment():
    comment=request.form['comment']
    ident=int(request.form['id'])
    # Error becuase database is expecting a value for message_id for this post
    query = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES (:comment, :user_id, :message_id, NOW(), NOW())"
    data={
        'comment':comment,
        'user_id':session['id'],
        'message_id':ident
        }
    mysql.query_db(query,data)
    return redirect('/wall')


app.run(debug=True)
