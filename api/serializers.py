from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Product, Category, Order, CartItem


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

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'


class ItemDetailSerializer(serializers.ModelSerializer):
	cart_items = serializers.SerializerMethodField()

	class Meta:
		model = CartItem
		fields = '__all__'

	def get_cart_items(self, obj):
		return OrderSerializer(obj.cartitem_set.all(), many=True).data

		
class OrderListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "order_id"
		)

	cart_items = serializers.SerializerMethodField()

	class Meta:
		model = Order
		fields = '__all__'

	def get_cart_items(self, obj):
		items = CartItem.objects.filter(order=obj)
		return ItemDetailSerializer(items, many=True).data

class OrderCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'
		