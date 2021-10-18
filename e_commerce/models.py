from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=100)
    

class Products(models.Model):
    pname = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
