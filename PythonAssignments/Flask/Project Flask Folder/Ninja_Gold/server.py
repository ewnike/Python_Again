from flask import Flask, render_template, redirect, request, session, flash
import random
from datetime import datetime, date, time

app = Flask(__name__)
app.secret_key = "MickeyMouse"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']= 0
    if "activity" not in session:
        session['activity'] = []
    length = len(session['activity'])
    return render_template('index.html', activity = session['activity'], length = length)

@app.route('/process_money', methods = ['POST'])
def process():
    building = request.form['building']
    currentactivity=""
    status = "win"
    if request.form['building'] == 'farm':
        change =random.randrange(10, 20)
        session['gold'] = session['gold'] + change
        currentactivity += "You have just earned" + " " + str(change) + " "+ "golds working on the farm!"

    elif request.form['building'] == 'cave':
        change=random.randrange(5,10)
        session['gold'] = session['gold'] + change
        currentactivity += "You have just earned" + " " + str(change) +" "+  "golds working in the cave!"

    elif request.form['building'] == 'home':
        change=random.randrange(2,5)
        session['gold'] = session['gold'] + change
        currentactivity += "You have just earned"+" "+ str(change) +" "+  "golds working at home!"

    elif request.form['building'] == 'casino':
        change=random.randrange(-50,50)
        session['gold'] = session['gold'] + change
        if change>0:
            currentactivity += "You have just earned" +" " + str(change) + " " +"golds at the casino. Let it ride!"
        elif change==0:
            status = "even"
            currentactivity += "You have just scratched at the casino. Better quit while ahead."
        elif change < 0:
            status = "loss"
            currentactivity += "You have just lost" + " "+ str(change)+ " " + "golds at the casino. Maybe go back to work..."

    now = str(datetime.now())
    now = now[:19]
    currentactivity += "(" + now + ")"
    activity_result = {"message":currentactivity, "class":status}
    session['activity'].append(activity_result)
    return redirect('/')

@app.route('/reset')
def reset():
    session['gold']= 0
    session['activity']= []
    return redirect('/')

app.run(debug=True)
