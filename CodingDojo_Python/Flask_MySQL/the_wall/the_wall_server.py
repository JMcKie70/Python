from flask import Flask, flash, render_template, redirect, session, request
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)

app.secret_key = "secret"

EMAIL = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')

@app.route('/')
def homepage():
	return render_template ('login_register.html')


@app.route('/login', methods = ['POST'])
def login():
	user_login_info ={'email':request.form['email'],'password':request.form['password']}
	query = "select * from users where email =:email"
	# this is just setting a variable so that we don't have to write it out later
	user = mysql.query_db(query, user_login_info)
	#uses the mysql connection to to call the dictionary is using the key at the email property (grab the email key and grab all the emails in the database that match the form email)

	if len(user) != 0:
		user = user[0]
	else:
		flash('incorrect email')
		return redirect('/')

	if not user:
		flash('no such email')
		return redirect('/')

	print bcrypt.check_password_hash(user['password'], user_login_info['password'])

	if not bcrypt.check_password_hash(user['password'], user_login_info['password']):
		flash('wrong password')
	 	return redirect('/')

	session['user'] = user

	return redirect('/wall')


@app.route('/register', methods= ['POST'])
def register ():
	user_register_info ={'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'password': request.form['password']}
	errors = False

	if len(user_register_info['email']) < 5 or not EMAIL.match(request.form['email']):
		flash('email must contain @ and a . and must not be blank')
		errors = True

	if len(user_register_info['password']) < 6:
		flash('password must contain be at least 6 characters long')
		errors = True

	if len(user_register_info['first_name']) < 2:
		flash('first name must contain be at least 6 characters long')
		errors = True

	if len(user_register_info['last_name']) < 2:
		flash('last name must contain be at least 6 characters long')
		errors = True

	if len(request.form['password_confirmation']) == user_register_info['password']:
		flash('passwords  must match')
		errors = True

	if errors:
		return redirect('/')

	query = """Insert into users(first_name,last_name,email,password, added, edited)
		values(:first_name, :last_name, :email, :password, now(), now())"""                  #this is a variable named query that when placed into mysql

	user_register_info['password'] = bcrypt.generate_password_hash(user_register_info['password'])

	user_id = mysql.query_db(query,user_register_info)

	new_query = """Select first_name, last_name, id from users
				where id = :id"""

	user_register_info['id'] = user_id

	session['user'] = mysql.query_db(new_query, user_register_info)[0]
	print session['user']
	return redirect('/wall')

@app.route('/wall') #method get is automatically default
def wall():
	if 'user' not in session:
		return redirect('/')

	messages_query = """Select messages.message, messages.added, messages.id,
						concat(users.first_name," ", users.last_name) as username
						from messages
						join users on users.id = messages.user_id
						order by messages.id desc"""

	messages = mysql.query_db(messages_query)

	comments_query = """Select comments.comment_text, comments.added, concat(users.first_name,' ', users.last_name) as username
						from comments
						join messages
						on comments.message_id = messages.id
						join users
						on comments.user_id = users.id
						where messages.id = {}"""


	# comments_query = """Select comments.comment_text, comments.added, comments.id,
	# 					concat(users.first_name," ", users.last_name) as username
	# 					from comments
	# 					join users on users.id = comments.user_id
	# 					order by comments.id desc"""

	# comments = mysql.query_db(comments_query)

	for message in messages:
		message['comments'] = []
		message['comments'] += mysql.query_db(comments_query.format(message['id'])) #concating instead pf appending so its not an array of arrays
		# print comments_query
		# print message['id']
		# print message['comments']
	return render_template('wall.html', wall_messages=messages)



@app.route('/message', methods= ['POST'])
def message():

	messages = {'user_id': request.form['user_id'],'message_text': request.form['message_text']}

	print request.form

	query = """Insert into messages(user_id, message, added, edited)
			values(:user_id, :message_text, now(), now())"""

	mysql.query_db(query, messages)

	return redirect('/wall')

@app.route('/comment', methods= ['POST'])
def comment():

	comments ={'user_id': request.form['user_id'],'message_id': request.form['message_id'],'comment_text': request.form['comment_text']}

	print 'comment'
	print comments['user_id']
	print request.form

	query = """Insert into comments(user_id, message_id, comment_text, added, edited)
			values(:user_id, :message_id, :comment_text, now(), now())"""


	mysql.query_db(query, comments)

	return redirect('/wall')


@app.route('/logout', methods = ['POST'])
def logout():
	session.pop('user')
	return redirect('/')

app.run(debug=True)






# select film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
# from actor
# left join film_actor on actor.actor_id = film_actor.actor_id
# left join film on film.film_id = film_actor.film_id
# left join film_category on film.film_id = film_category.film_id
# left join category on category.category_id = film_category.category_id
# where category.name = 'action'
# and actor.first_name = 'sandra'
# and actor.last_name = 'kilmer'
# ;
