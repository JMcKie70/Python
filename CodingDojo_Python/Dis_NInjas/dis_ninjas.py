from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def no_ninjas():
	return render_template("none_ninjas.html", phrase="No ninjas here", ninjas_property="none")

@app.route('/ninjas')
def four_ninjas():
	return render_template("none_ninjas.html")

@app.route('/ninjas/<variable>')
def ninja_megan(variable):
	if variable == "blue":
		return render_template('ninja_megan.html', orange_property="none", red_property="none", purple_property="none", hack_property="none")
	elif variable == "orange":
		return render_template('ninja_megan.html', blue_property="none", red_property="none", purple_property="none", hack_property="none")
	elif variable == "red":
		return render_template('ninja_megan.html', blue_property="none", orange_property="none", purple_property="none", hack_property="none")
	elif variable == "purple":
		return render_template('ninja_megan.html', blue_property="none", orange_property="none", red_property="none", hack_property="none")
	else:
		return render_template('ninja_megan.html', blue_property="none", orange_property="none", red_property="none", purple_property="none")

app.run(debug=True)
