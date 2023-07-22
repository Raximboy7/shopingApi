from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, buy, BuyViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
     path('products/<int:pk>/buy/', buy, name='buy'),
     path('buy/', BuyViewSet.as_view({'get': 'list'}))
]
