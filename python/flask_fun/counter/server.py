from flask import Flask, render_template,session

app= Flask(__name__)



@app.route('/')
def count(): 
    if not session['count']:
        session['count']=0
    session['count']+=1
    return render_template('index.html', count=session['count'])

@app.route('/add')
def doublecount():
    session['count']+=2
    return render_template('index.html', count=session['count'])

@app.route('/reset')
def reset():
    session['count']=1
    return render_template('index.html', count=session['count'])


app.secret_key = "secrey"
app.run(debug=True)