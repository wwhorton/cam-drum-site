from django.contrib import admin
from .models import Article, ArticleAdmin, Card

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Card)
