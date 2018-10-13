from rest_framework import serializers
from django.contrib.auth.models import User

from user.serializers import UserSerializer
from .models import Profiles

class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profiles
        fields = (
            'user',
            'bio',
            'image',
            'gender'
        )

    def create(self, validated_data):
        profiles, created = Profiles.objects.update_or_create(**validated_data)

        profiles.save()
        return profiles
