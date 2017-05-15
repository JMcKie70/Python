from __future__ import unicode_literals

from django.db import models
import re
REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validate_user(self, post_data):
		error_message = []
		if len(post_data['email']) < 1:
			error_message.append('You must enter a valid email.')
		if REGEX.match(post_data['email']) == None:
			error_message.append('Invalid email.')
		if error_message:

			return{"error": error_message}
		else:
			created_user = User.objects.create(email = post_data["email"])

		return{"the_user": created_user}

class User(models.Model):
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

# Create your models here.

