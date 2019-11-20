from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('myboard.Post', on_delete=models.CASCADE, related_name='comments')
    writer = models.CharField(max_length=200)
    text = models.TextField()
    commented_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

