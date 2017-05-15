from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
	return render_template("index.html")
  
@app.route('/result', methods=['POST'])
def create_user():
  if len(request.form['name']) < 1:
    flash("Please provide your name.")
    return redirect('/')# just pass a string to the flash function
  else:
    flash("Success! Your name is {}".format(request.form['name']))
  name = request.form['name'] # just pass a string to the flash function
  if len(request.form['comment']) < 1:
    flash("Please provide your comments.")
    return redirect('/') # just pass a string to the flash function
  elif len(request.form['comment']) > 120:
  	flash("Please limit comments to less than 120 characters.")
  	return redirect('/')
  else:
    flash("Success! Your comments are {}".format(request.form['comment']))
  comment = request.form['comment']
  location = request.form['location']
  language = request.form['language']
  
  return render_template("result.html", name = name, location = location, language = language, comment = comment)

app.run(debug=True) # run our server
