from .serializer import ProductSerializer
from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from ..models import Product
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from ..query import filter_product, get_product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = filter_product()
    serializer_class = ProductSerializer

    def update(self, request, pk):
        serializer = ProductSerializer(data=request.data)
        print(request.data["title"])
        # print(serializer.get("title"])
        if serializer.is_valid():
            product = Product.objects.filter(id=pk).update(title=request.data["title"],slug=request.data["slug"] ,\
                                                             description= request.data["description"], \
                                                                image=request.data["image"] ,status=request.data["status"]
                                                                      )
            
            
            
            
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)