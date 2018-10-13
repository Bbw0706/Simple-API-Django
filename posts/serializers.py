from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Posts
from user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False, allow_null=True)
    created_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Posts
        fields = (
            'id',
            'title',
            'description',
            'likes',
            'created_at',
            'created_by',
            'created_by_id',
        )


    def create(self, validated_data):
        posts = Posts.objects.create(**validated_data)

        posts.save()
        return posts
