from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, BuyList, BuyViewSet, BuyDetail

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'buy', BuyViewSet )

urlpatterns = [
    path('', include(router.urls)),
     path('products/<int:pk>/buy/', BuyList.as_view(), name='buy'),
     path('buy/', BuyViewSet.as_view({'get': 'list'})),
     path('buy/detail/<int:pk>/', BuyDetail.as_view())
]
