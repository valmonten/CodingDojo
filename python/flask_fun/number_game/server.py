from flask import Flask, render_template, session, request, redirect
import random

app= Flask(__name__)

app.secret_key = "supersecret"

@app.route('/')
def something():

    session['pandora']=random.randint(1,100)
    

    return render_template('index.html', rando=session['pandora'])

@app.route('/guess', methods=["POST"])
def guess():

    guess=int(request.form['guess'])

    if guess<session['pandora']:
        message = "Your guess was too low"

    elif guess>session['pandora']:
        message = "Your guess was too high"

    else:
        message = "You guessed "+str(guess)+" and it was "+str(session['pandora'])

    return render_template('index.html', message=message, rando=session['pandora'])

@app.route('/replay', methods=["POST"])
def replay():
    session.pop('pandora')
    return redirect('/')



app.run(debug=True)