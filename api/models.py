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
	img = models.ImageField(blank = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	brand = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Order(models.Model):
	order_id = models.CharField(max_length=10)
	date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.BooleanField() #True for active order
	

	def __str__(self):
		return str(self.id) + " " + str(self.user)

class CartItem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.order)

class Address(models.Model):
	area = models.CharField(max_length=100, blank=True, null=True)
	block = models.CharField(max_length=100, blank=True, null=True)
	street = models.CharField(max_length=100, blank=True, null=True)
	building = models.IntegerField(blank=True, null=True)
	phone_number = models.CharField(max_length=8, blank=True, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

