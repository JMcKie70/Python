from flask import Flask, render_template, redirect, session, request, flash, url_for
import datetime, random
app=Flask(__name__)
app.secret_key="NinjaGold"

@app.route('/')
def index():
	if "gold" not in session:
		session["gold"] = 0
	if "messages" not in session:
		session["messages"] = []
	return render_template("n_gold.html")

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['location'] == 'farm':
		earned_gold = random.randint(10, 20)
	
	elif request.form['location'] == 'cave':
		earned_gold = random.randint(5, 10)
	
	elif request.form['location'] == 'house':
		earned_gold = random.randint(2, 5)
	
	elif request.form['location'] == 'casino':
		earned_gold = random.randint(-50, 50)

	if earned_gold < 0:
		new_message = 'Entered a casino and lost ' + str(-earned_gold) + ' gold coins... Ouch. ' + str(datetime.datetime.now())
		color = 'red'
	else:
		new_message = 'Earned ' + str(earned_gold) + " gold coins from the " + request.form['location'] + "! " + str(datetime.datetime.now())
		color = 'green'

	session['gold'] += earned_gold
	message_dictionary = {'content': new_message, 'color': color}
	session['messages'].insert(0, message_dictionary)
	return redirect('/')

app.run(debug=True)

