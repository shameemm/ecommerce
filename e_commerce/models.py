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
    image = models.ImageField(null=True, blank=True,upload_to='static/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    