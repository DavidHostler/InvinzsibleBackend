from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ProductDetailView,ProductListView, OrderDetailView, OrderListView
#router = routers.DefaultRouter()
#router.register('product', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('', ProductListView.as_view()),
    path('<pk>', ProductDetailView.as_view()),
    path('<pk>', OrderDetailView.as_view()),

]