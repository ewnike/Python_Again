from flask import Flask , render_template, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('ninja.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)
