from .serializer import CommentSerializer
from rest_framework import viewsets, permissions
from ..models import Comments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()] 
        return [permissions.IsAuthenticatedOrReadOnly()]