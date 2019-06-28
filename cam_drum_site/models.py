from django.db import models
from django.contrib import admin


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='')
    text = models.TextField()
    blurb = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/')


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
