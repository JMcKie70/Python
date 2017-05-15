from __future__ import unicode_literals

from django.db import models
import re
REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt
# Create your models here.
class UserManager(models.Manager):
	def register_user(self, post_data):
		error_message = []
		if len(post_data['first_name']) < 2 or post_data['first_name'].isalpha() == False:
			error_message.append('Must be at least 2 or more letters.')
		if len(post_data['last_name']) < 2 or post_data['last_name'].isalpha() == False:
			error_message.append('Must be at least 2 or more letters.')
		if REGEX.match(post_data['email']) == None:
			error_message.append('Invalid email format.')
		if len(post_data['password']) < 8:
			error_message.append('Must be at least 8 or more letters.')
		if post_data['confirm_pw'] != post_data['password']:
			error_message.append('Confirmation must match password.')

		if error_message:
			return{"error": error_message}
		else:
			hashed = bcrypt.hashpw(post_data['password'].encode("utf-8"), bcrypt.gensalt())
			created_user = User.objects.create(first_name = post_data['first_name'], last_name = post_data['last_name'], email = post_data["email"], password = hashed)
			print created_user.first_name
		return{"the_user": created_user}

	def login_user(self, post_data):
		error_message = []
		entered_pass=post_data["password"]
		hashed = User.objects.get(email= post_data['email']).password

		if REGEX.match(post_data['email']) == None:
			error_message.append('Invalid email format.')
		if not User.objects.filter(email = post_data['email']):
			error_message.append('Invalid email.')
		if len(post_data['password']) < 8:
			error_message.append('Must be at least 8 or more letters.')
		if bcrypt.hashpw(entered_pass.encode('utf-8'), hashed.encode('utf-8')) != hashed:
			error_message.append('Invalid password.')

		if error_message:
			return{"error": error_message}
		else:
			loggedin_user = User.objects.get(email=post_data['email']).id

		return{"the_user": loggedin_user}

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
