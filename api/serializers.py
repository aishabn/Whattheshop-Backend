from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Product, Category, Order, CartItem, Address


class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	address = AddressSerializer()
	class Meta:
		model = User
		fields = ['id','username', 'first_name', 'last_name', 'email', 'address']

class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields =['id','name','price','description','img','brand']

class CategoryDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
	products = ProductListSerializer(many=True)
	class Meta:
		model = Category
		fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = CartItem
		fields = ['item','quantity']

	



class OrderCreateSerializer(serializers.ModelSerializer):
	cart_items = serializers.SerializerMethodField()

	class Meta:
		model = Order
		fields = ['cart_items']

	def get_cart_items(self, obj):
		return CartItemSerializer(obj.cartitem_set.all(), many=True).data
		
	

class OrderDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Order
		fields = '__all__'


		