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
	OrderListSerializer
)

from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Product, Category, Order

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProductListSerializer(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name', 'description']

class ProductDetailSerializer(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

class CategoryListSerializer(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name']

class OrderListSerializer(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['order_number']

class OrderDetailSerializer(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = OrderListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

