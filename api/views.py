from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)
from .serializers import (
	UserCreateSerializer,
	ProductListSerializer,
	ProductDetailSerializer,
	CategoryListSerializer,
	# OrderListSerializer,
	UserSerializer,
	OrderDetailSerializer,
	OrderCreateSerializer,
	
)
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Product, Category, Order
from django.http import HttpResponse, JsonResponse

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class UserView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'

#ProductListView -> CategoryListView


class ProductDetailView(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name']

class OrderListView(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderCreateSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['id']

class OrderDetailView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class OrderCreateView(CreateAPIView):
	serializer_class = OrderCreateSerializer

	def post(self, request, format=None):
		serializer = OrderCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors)


