from __future__ import unicode_literals
from django.db import models

class ProductManager(models.Manager):
	def build_product(self, postData):
		error_msgs = []
		try:
			User.objects.get(name=postData['name'])
			error_msgs.append("That product already exists.")		
		except:
			pass
		if len(postData['name']) < 2:
			error_msgs.append("Name is too short!")
			print "2"
		if len(postData['description']) < 5:
			error_msgs.append("Description is too short!")
			print "3"
		if len(postData['price']) < 4:
			error_msgs.append("enter full price.")
			print "4"
		if error_msgs:
			return {'errors':error_msgs}
		else:
			product = Products.objects.create(name= postData['name'], description= postData['description'], price= postData['price'])
			return {'product' : product.name, 'description' : product.description, 'price' : product.price, 'product_id' : product.id}

	# def update(self, postData):
	# 	product = Products.objects.get(name= postData['name'], description= postData['description'], price= postData['price'])
	# 	return {'product' : product.name, 'description' : product.description, 'price' : product.price, 'product_id' : product.id}

class Products(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
