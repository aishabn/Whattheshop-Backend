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
	OrderListSerializer,
	UserSerializer,
	ItemDetailSerializer,
	OrderCreateUpdateSerializer
)
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Product, Category, Order

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProductListView(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name', 'description']

class ProductDetailView(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

class UserSerializerView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name']

class OrderListView(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['order_id']

class OrderDetailView(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class OrderCreateView(CreateAPIView):
	serializer_class = OrderCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		
class OrderUpdateView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'


