from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=False)
    likes = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'posts'
        ordering = ('created_at',)
