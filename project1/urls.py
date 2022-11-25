from django.contrib import admin
from django.urls import path, include
from api_practice import views
from rest_framework.routers import DefaultRouter


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register('shop', views.ShopViewSet, basename='shop')
router.register('supplier', views.SupplierViewSet, basename='supplier')
router.register('order', views.OrderViewSet, basename='order')

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]