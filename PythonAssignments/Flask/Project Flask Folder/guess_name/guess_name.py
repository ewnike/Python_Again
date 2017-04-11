from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def get_name():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def create_name():
    print "Got it!!"
    name = request.form['name']
    return redirect('/')

app.run(debug=True)
