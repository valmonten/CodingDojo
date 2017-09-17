from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)

app.secret_key= 'sfljk32fn'

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def create_user():
    print "Got User"
    name=request.form['namey']
    location=request.form['location']
    language=request.form['language']
    comments=request.form['comments']
    if len(name)>0:
        # flash("Success!")
        if len(comments)>120:
            flash("Comments cannot be longer than 120 characters")
            return render_template('index.html')
        else:
            return render_template('info.html', name=name, location=location, language=language, comments=comments)    
    else:
        flash("Name cannot be empty")
        print
        return render_template('index.html')
app.run(debug=True)