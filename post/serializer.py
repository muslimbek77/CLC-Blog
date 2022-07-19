from rest_framework import serializers
from post.models import Post
from author.serializer import AuthorDetailSerializer

class PostSerializer(serializers.ModelSerializer):
    author = AuthorDetailSerializer()
    class Meta:
        model = Post
        fields = "__all__"
