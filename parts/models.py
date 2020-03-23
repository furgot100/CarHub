from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


