import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=400)

    def __str__(self):
        return self.title

    def publish_date(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)