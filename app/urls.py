from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ProductViewSet, OrderViewSet, CartViewSet
#ProductDetailView,ProductListView, OrderDetailView, OrderListView, 

 



router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('orders', views.OrderViewSet)
router.register('cart',views.CartViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
    #path('', ProductListView.as_view()),
    #path('<pk>', ProductDetailView.as_view()),
    #path('<pk>', OrderDetailView.as_view()),

]
