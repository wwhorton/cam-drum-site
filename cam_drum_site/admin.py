from django.contrib import admin
from .models import Topic, TopicAdmin

# Register your models here.
admin.site.register(Topic, TopicAdmin)
