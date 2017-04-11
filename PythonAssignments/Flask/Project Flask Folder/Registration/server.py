from flask import Flask, render_template, redirect, session, flash, request
import re

app=Flask(__name__)
app.secret_key = "mickeymouse"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birthdate= request.form['birthdate']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['password']

    isValid = True

    if len(first_name)<2:
        flash("Please enter a valid  first name. It must be longer than 2 characters.")
        isValid = False
    elif not  str.isalpha(str(first_name)):
        flash("Please enter a valid first name.")
        isValid = False

    if len(last_name)<2:
        flash("Please enter a valid last name. It must be longer than 2 characters.")
        isValid = False
    elif not  str.isalpha(str(last_name)):
        flash("Please enter a valid first name.")
        isValid = False

    if len(email) < 1:
        flash("Please enter email address.")
        isValid = False
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email address. Please re-enter.")
        isValid = False

    if len(password) < 9:
        flash("Password must be longer than 8 characters.")
        isValid = False
    elif (password) != (confirm_password):
        flash("Password and confirmation do not match.")
        isValid = False

    if not isValid:
        return redirect('/')

    else:
        return render_template('success.html', first_name = first_name, last_name = last_name, birthdate = birthdate, email=email, password=password)

app.run(debug=True)
