from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=8, decimal_places=3)
	description = models.TextField()
	img = models.ImageField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	brand = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class CartItem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
	order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Order(models.Model):
	order_id = models.CharField(max_length=10)
	date = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# item = models.ForeignKey(CartItem, on_delete=models.CASCADE)

	def __str__(self):
		return self.order_id
