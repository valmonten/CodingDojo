from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'SECRET'
mysql = MySQLConnector(app,'books')

@app.route('/')
def index():
    thingys = mysql.query_db("SELECT * FROM books")
    print thingys
    print thingys[0]['title']
    return render_template('index.html', thingys=thingys)

@app.route('/add')
def ab():
    return render_template('add.html')

@app.route('/adding', methods=['POST'])
def i23u4ht():
    title= request.form['title']
    author= request.form['author']
    query="INSERT INTO books(title,author,created_at,updated_at) VALUES(:title,:author,NOW(),NOW())"
    data={
        'author':author,
        'title':title
    }
    mysql.query_db(query,data)
    return redirect('/')
# @app.route('/destroy/<bookid>', methods=["POST"])
# def destroyer(bookid):
#     query='DELETE'

app.run(debug=True)