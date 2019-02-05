from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.views import UserView, UserCreateAPIView, CategoryDetailView, CategoryListView,CartItemCreateView, PastOrderListView, PastOrderDetailView, OrderCreateView


urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('api.urls')),

	path('api/list/', CategoryListView.as_view(), name='api-category'),
	path('api/list/<int:cat_id>/', CategoryDetailView.as_view(), name='api-detail'),
	path('api/item/', CartItemCreateView.as_view(), name='api-cart-items'),
	path('api/order/', PastOrderListView.as_view(), name='api-order'),
	path('api/order/detail/<int:order_id>/', PastOrderDetailView.as_view(), name='api-order-detail'),
	path('api/order/create/', OrderCreateView.as_view(), name='api-order-create'),
	path('api/profile/<int:user_id>', UserView.as_view(), name='api-profile'),

]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)