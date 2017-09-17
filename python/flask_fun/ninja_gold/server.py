from flask import Flask, session, redirect, render_template, request
import random, time
app = Flask(__name__)

app.secret_key = "supersecret"

@app.route('/')
def start():
    if not session.get('gold'):
        session['gold']=0    
    if not session.get('activity'):
        session['activity']=[]
    if not session.get('rando'):
        session['rando']=0
    return render_template('index.html', gold=session['gold'], activity=session['activity'], rando=session['rando'])
@app.route('/process_money', methods=['POST'])
def adding():
    lame=request.form['location']


    if lame=="farm":
        session['rando']=random.randint(10,20)
        session['gold']+=session['rando']
        session['activity'].append("You earned "+str(session['rando'])+" gold from the "+lame+"! on "+time.strftime('%c'))
        print session['activity']
    if lame=="cave":
        session['rando']=random.randint(5,10)
        session['gold']+=session['rando']
        session['activity'].append ("You earned "+str(session['rando'])+" gold from the "+lame+"! on "+time.strftime('%c'))
    if lame=='house':
        session['rando']=random.randint(2,5)
        session['gold']+=session['rando']
        session['activity'].append("You earned "+str(session['rando'])+" gold from the "+lame+"! on "+time.strftime('%c'))
    if lame=="casino":
        session['rando']=random.randint(-50,50)
        session['gold']+=session['rando']
        if session['rando'] >=0:
            session['activity'].append("You earned "+str(session['rando'])+" gold from the "+lame+"! on "+time.strftime('%c'))
        else:
            session['activity'].append("You lost "+str(session['rando'])+" gold from the "+lame+"! on "+time.strftime('%c'))
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold')
    session.pop('activity')
    return redirect('/')

app.run(debug=True)