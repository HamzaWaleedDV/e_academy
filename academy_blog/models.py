from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    cover_image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    subject = HTMLField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title