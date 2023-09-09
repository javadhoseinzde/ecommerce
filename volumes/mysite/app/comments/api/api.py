from .serializer import CommentSerializer
from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from ..models import Product
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from app.shop.query import get_comment
from ..models import Comments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

        
    def update(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        username = request.user.mobile
        print(username)
        # print(serializer.get("title"])
        if serializer.is_valid():
            pass
            
            
            
            
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

