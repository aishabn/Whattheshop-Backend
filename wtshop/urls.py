from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.views import UserCreateAPIView, ProductListSerializer, ProductDetailSerializer, CategoryListSerializer, OrderListSerializer, OrderDetailSerializer


urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('api.urls')),
	path('api/list/', ProductListSerializer.as_view(), name='api-list'),
	path('api/detail/<int:product_id>/', ProductDetailSerializer.as_view(), name='api-detail'),
	path('api/category/', CategoryListSerializer.as_view(), name='api-category'),
	path('api/order/', OrderListSerializer.as_view(), name='api-order'),
	path('api/order/detail/<int:order_id>/', OrderDetailSerializer.as_view(), name='api-order-detail'),

]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)