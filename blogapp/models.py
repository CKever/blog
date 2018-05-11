from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)


class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)


class Post(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:detail', kwargs={'pk': self.pk})
    title = models.CharField(max_length=100)

    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-created_time']

