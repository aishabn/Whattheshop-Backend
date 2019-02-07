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
	# OrderListSerializer,
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
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'

	def get(slef,request):
		return JsonResponse(UserSerializer(request.user).data)

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


class PastOrderListView(ListAPIView):
	# queryset = Order.objects.all()
	serializer_class = OrderCreateSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['id']

	def get_queryset(self):
		return Order.objects.filter(user=self.request.user)

class PastOrderDetailView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class OrderCreateView(APIView):
	# serializer_class = OrderCreateSerializer

	def post(self, request, format=None):
		print(request.data)
		order = Order.objects.create(user=request.user)
		for item in request.data:
			i = CartItem.objects.create(order=order, item_id=item['item_id'], quantity=item['quantity'])
			# print(item)
		# serializer = OrderCreateSerializer(user=request.user)
		# if serializer.is_valid():
		# 	serializer.save()
			# return JsonResponse(serializer.data)
		return JsonResponse({"list":"list"},safe=False)

