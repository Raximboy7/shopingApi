from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['GET'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(slug=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]




class BuyList(ListCreateAPIView):
    serializer_class = BuySerializer

    def get(self, request, pk=None):
        if request.method == 'GET':
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = BuySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer


class BuyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer