from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('my_name.html')
@app.route('/projects')
def showntell():
    return render_template('projects.html')
@app.route('/about')
def rogerdoger():
    return render_template("about.html")
app.run(debug=True)