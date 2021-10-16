from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=100)
    