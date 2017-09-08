from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def indexing():
    return render_template("index.html")
@app.route('/ninjas')
def show():
    return render_template("ninjas.html")
@app.route('/dojos/new')
def showing():
    return render_template("dojo_new.html")
app.run(debug=True)