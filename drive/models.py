from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    file = models.FileField(upload_to='media')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file