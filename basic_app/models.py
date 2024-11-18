import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    created = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.title