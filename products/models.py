from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField()
    gallery = models.ForeignKey('galleries.Gallery', on_delete=models.SET_NULL, null=True, blank=True)