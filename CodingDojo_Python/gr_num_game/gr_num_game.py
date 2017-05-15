from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/')
def random_number():
	import random
	session['random_num'] = random.randint(1,100)
	session['response'] = ''
	return render_template("gr_num_game.html")
# this route will handle our form submission
	
# notice how we defined which HTTP methods are allowed by this route
@app.route('/guess', methods=['POST'])
def compare():
	print "Got Post Info"

	number = int(request.form['number'])
	if number > session['random_num']:
		session['response'] = 'high'
	elif number < session['random_num']:
		session['response'] = 'low'
	else:
		session['response'] = 'correct'
	return render_template('gr_num_game.html', number=number)
@app.route('/retry', methods=['post'])
def retry():
  return redirect("/")
app.run(debug=True) # run our server
