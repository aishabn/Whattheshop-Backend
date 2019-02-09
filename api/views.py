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
	CategoryDetailSerializer,
	CategoryListSerializer,
	UserSerializer,
	OrderDetailSerializer,
	OrderCreateSerializer,
	CartItemSerializer,

)
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Product, Category, Order, CartItem
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView



class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class UserView(RetrieveAPIView):
	serializer_class = UserSerializer

	def get(self,request):
		user =  request.user
		return JsonResponse(UserSerializer(user).data)

#ProductListView -> CategoryListView

class CategoryDetailView(RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'cat_id'

class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name']

class CartItemCreateView(CreateAPIView):
	serializer_class = CartItemSerializer

	def perform_create(self, serializer):
		order, created = Order.objects.get_or_create(user=self.request.user, status=True )
		serializer.save(order=order)

class PastOrderListView(ListAPIView):
	serializer_class = OrderCreateSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['id']

	def get_queryset(self):
		return Order.objects.filter(user=self.request.user, status=False)

class PastOrderDetailView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class CheckoutView(APIView):
	def get(self, request, format=None):
		order = Order.objects.get(user=request.user, status=True)
		order.status = False
		order.save()
	
		return JsonResponse({"list":"list"},safe=False)

class CartItemDeleteView(DestroyAPIView):
	queryset = CartItem.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'

