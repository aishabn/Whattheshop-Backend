from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Product, Category, Order


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

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', ]

class ProductListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "product_id"
		)
	
	class Meta:
		model = Product
		fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
	products = ProductListSerializer(many=True)
	class Meta:
		model = Category
		fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'