from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ninja')
def peekaboo():
    ninja="tmnt.png"
    return render_template("all_four.html", ninja=ninja)
@app.route('/ninja/<color>')
def ninja(color):
    # print color
    if color=="blue":
        ninja="leonardo.jpg"
    elif color=="red":
        ninja= "raphael.jpg"
    elif color=="orange":
        ninja="michelangelo.jpg"
    elif color=="purple":
        ninja="donatello.jpg"
    else:
        ninja="notapril.jpg"
    return render_template("all_four.html", ninja=ninja)

app.run(debug=True)