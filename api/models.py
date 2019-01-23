from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	category_choices = [('indoor','Indoor'),('outdoor','Outdoor'),('apparel','Apparel'),('footwear','Footwear'),('fitness','Fitness'),('sports','Sports')]

	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=8, decimal_places=3)
	description = models.TextField()
	img = models.ImageField()
	category = models.CharField(max_length=200, choices=category_choices)
	brand = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class CartItem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

