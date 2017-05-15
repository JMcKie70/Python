from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

@app.route('/')
def index():
	session['number'] = session.get('number', 0)
	session['number'] += 1
	return render_template("counter.html",counter = session['number'])
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninja', methods=['GET','POST'])
def ninja():
	session['number'] = session['number'] + 1
	return redirect('/')
@app.route('/reset', methods=['GET','POST'])
def reset():
	session['number'] = -1
	return redirect('/')
app.run(debug=True) # run our server
