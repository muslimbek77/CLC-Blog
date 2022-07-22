# Create your views here.
from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from author.models import Author
from post.models import Post

from author.serializer import AuthorDetailSerializer
from helpers.pagination import CustomPagination
from post.serializers import PostSerializer
"""
TODO:
    - POPULAR DETAIL POST
    - FOR YOU DETAIL POST
"""


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PopularPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = queryset.filter(is_popular=True)

        return queryset


class ForYouPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = queryset.filter(for_you=True)

        return queryset
