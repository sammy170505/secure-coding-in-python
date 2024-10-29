from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        lookup_field = 'slug'
        fields = '__all__'

    created = serializers.DateTimeField(format='%a, %d %b %Y')
