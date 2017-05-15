from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]')
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
	return render_template("reg_form.html")
  
@app.route('/process', methods=["POST"])
def submit():
  if len(request.form['email']) < 1:
    flash("All fields are required and must not be blank.")
    return redirect('/') 
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Email should be a valid email.")
    return redirect('/')
  else:
    email = request.form['email']

  if len(request.form['first_name']) < 1:
    flash("All fields are required and must not be blank.")
    return redirect('/') 
  elif request.form['first_name'].isalpha() == 'false':
    flash("First and Last Name cannot contain any numbers.")
    return redirect('/') 
  else:
    first_name = request.form['first_name']

  if len(request.form['last_name']) < 1:
    flash("All fields are required and must not be blank.")
    return redirect('/') 
  elif request.form['last_name'].isalpha() == 'false':
    flash("First and Last Name cannot contain any numbers.")
    return redirect('/') 
  else:
    last_name = request.form['last_name']

  if len(request.form['password']) < 1:
    flash("All fields are required and must not be blank.")
    return redirect('/') # just pass a string to the flash function
  elif len(request.form['password']) < 8:
    flash("Password should be more than 8 characters.")
    return redirect('/')
  elif not PASSWORD_REGEX.match(request.form['password']):
    flash("Password should contain at least 1 uppercase letter and 1 numeric value.")
  else:
    password = request.form['password']

  if len(request.form['pw_confirm']) < 1:
    flash("All fields are required and must not be blank.")
    return redirect('/') # just pass a string to the flash function
  elif request.form['pw_confirm'] != password:
    flash("Password and Password Confirmation should match.")
    return redirect('/')
  else:
    pw_confirm = request.form['pw_contirm']
    flash("Thanks for submitting your information.")
    return redirect('/') 
  
app.run(debug=True) # run our server



