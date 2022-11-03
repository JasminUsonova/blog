from enum import unique
from turtle import title
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title= models.CharField(max_length=255, unique=True)

    def __str___(self):
        return f"{self.title:.30}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_draft = models.BooleanField(default=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField("posts.Tag")
    main_image=models.ImageField(upload_to="posts_images/", null=True, blank=True)

    def __str___(self):
        return f"{self.title:.30}"

    def save(self, *args, **kwargs):
        if not self.is_draft and not self.published_at:
            self.published_at=timezone.now()
        super().save(*args, **kwargs)