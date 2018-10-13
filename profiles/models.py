from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    class Meta:
        db_table = 'profile'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    bio = models.CharField(name="bio", max_length=128, null=True)
    gender = models.CharField(name="gender", max_length=128, null=True)
    image = models.TextField(name="image", max_length=128, null=True)

    def __str__(self):
        return self.user.first_name
