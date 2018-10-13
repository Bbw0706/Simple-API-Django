from django.db import models
from django.contrib.auth.models import User

from posts.models import Posts

class Comments(models.Model):
    def __str__(self):
        return self.text

    post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField(null=False, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'comments'
