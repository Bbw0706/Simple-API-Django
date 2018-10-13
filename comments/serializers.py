from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Comments
from posts.models import Posts

from user.serializers import UserSerializer
from posts.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)
    created_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    post = PostSerializer(required=False, read_only=True)
    post_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Comments
        fields = (
            'id',
            'text',
            'created_by',
            'created_by_id',
            'post',
            'post_id',
        )

    def create(self, validated_data):
        comments = Comments.objects.create(**validated_data)

        post_id = validated_data.get("post_id")
        validated_data.pop("post_id", None)
        post = Posts.objects.filter(id = post_id).first()
        comments.post = post

        comments.save()
        return comments
