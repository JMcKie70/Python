from __future__ import unicode_literals
from django.db import models

import bcrypt

class UserManager(models.Manager):
	def register_user(self, post_data):
		error_message = []
		if len(post_data['name']) < 3:
			error_message.append('Must be at least 3 characters.')
		if len(post_data['user_name']) < 3:
			error_message.append('Must be at least 3 characters.')
		if len(post_data['password']) < 8:
			error_message.append('Must be at least 8 characters.')
		if post_data['confirm_pw'] != post_data['password']:
			error_message.append('Please confirm password.')

		if error_message:
			return{"error": error_message}
		else:
			hashed = bcrypt.hashpw(post_data['password'].encode("utf-8"), bcrypt.gensalt())
			created_user = User.objects.create(name = post_data['name'], user_name = post_data['user_name'], password = hashed)
			print created_user.name
			return{"the_user": created_user}

	def login_user(self, post_data):
		error_message = []
		entered_pass=post_data["password"]
		hashed = User.objects.get(user_name = post_data['user_name']).password

		if len(post_data['password']) < 8:
			error_message.append('Must be at least 8 characters.')
		if bcrypt.hashpw(entered_pass.encode('utf-8'), hashed.encode('utf-8')) != hashed:
			error_message.append('Invalid password.')

		if error_message:
			return{"error": error_message}
		else:
			loggedin_user = User.objects.get(user_name=post_data['user_name']).id

		return{"the_user": loggedin_user}

class User(models.Model):
	name = models.CharField(max_length=45)
	user_name = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
