from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Post
from .serializers import PostSerializer


class IsAuthorReadOnly(BasePermission):
    """only authors should read posts"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated is True:
            return False
        return request.method in SAFE_METHODS and request.user.profile.is_writer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthorReadOnly]
