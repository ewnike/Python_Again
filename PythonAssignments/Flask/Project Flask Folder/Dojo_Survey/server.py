from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_data', methods = ['POST'])
def form():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('show.html', name=name, location=location, language=language, comments=comments)

app.run(debug = True)
