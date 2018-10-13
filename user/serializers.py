from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')


    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data.get('email'),
            first_name = validated_data.get('first_name'),
            password = validated_data.get('password'),
            username = validated_data.get('email'),
            last_name = validated_data.get('last_name')
        )

        return user
