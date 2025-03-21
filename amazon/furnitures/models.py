from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    material = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name