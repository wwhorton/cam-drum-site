from django.db import models
from django.contrib import admin


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='')
    text = models.TextField()


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
