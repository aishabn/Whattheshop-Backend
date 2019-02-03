from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.views import UserView, UserCreateAPIView, ProductDetailView, CategoryListView, OrderListView, OrderDetailView, OrderCreateView


urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('api.urls')),

	path('api/list/', CategoryListView.as_view(), name='api-category'),
	path('api/list/<int:product_id>/', ProductDetailView.as_view(), name='api-detail'),
	path('api/order/', OrderListView.as_view(), name='api-order'),
	path('api/order/detail/<int:order_id>/', OrderDetailView.as_view(), name='api-order-detail'),
	path('api/order/create/', OrderCreateView.as_view(), name='api-order-create'),
	path('api/profile/<int:user_id>', UserView.as_view(), name='api-profile'),

]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)