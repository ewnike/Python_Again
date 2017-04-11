from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key ='MickeyMouse'

@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')


@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
