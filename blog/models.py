from django.db import models
from django.urls import reverse

from core import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.post.pk)])
