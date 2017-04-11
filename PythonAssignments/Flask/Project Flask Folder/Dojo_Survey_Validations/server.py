from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key= "%V7O11Z'1Z;e]80"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_data', methods = ['POST'])
def form():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    isValid = True
    if len(name)<2:
        flash("Please enter a valid name It must be longer than 2 characters.")
        isValid = False
    if len(comments)<1:
        flash("Please add a comment. Comments are necessary so we can serve you better!")
        isValid=False
    if not isValid:
        return redirect('/')
    else:
        return render_template('show.html', name=name, location=location, language=language, comments=comments)


@app.route('/home')
def reset():
    return redirect('/')

app.run(debug = True)
