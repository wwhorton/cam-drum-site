from django.db import models


# Create your models here.
class Topic(models.Model):
    topic_title = models.CharField(max_length=200)
    topic_text = models.TextField()
