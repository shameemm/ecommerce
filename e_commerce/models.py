from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=100)

class Catogory(models.Model):
    category = models.CharField(max_length=100)

class Category(models.Model):
    category = models.CharField(max_length=100, primary_key=True)
    

class Products(models.Model):
    pname = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default='image/1.jpg', blank=True)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
