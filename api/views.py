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
)
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Product


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

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

