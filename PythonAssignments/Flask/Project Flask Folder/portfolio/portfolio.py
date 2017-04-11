from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/final')
def final_statement():
    return render_template('final.html')

app.run(debug=True)
