from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendly')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    # print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'age': int(request.form['age'])
            #  'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<friend_id>')
def show(friend_id):
    query = 'SELECT * FROM friends WHERE id = :specific_id'
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query,data)
    # print friends[0]
    return render_template('friend_search.html', one_friend=friends[0])

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')



app.run(debug=True)
