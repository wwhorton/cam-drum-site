from django.contrib import admin
from .models import Article, ArticleAdmin

# Register your models here.
admin.site.register(Article, ArticleAdmin)
