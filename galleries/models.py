from django.db import models

# Create your models here.
class Background(models.Model):
    image = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=20)
    recommend = models.BooleanField(default=False)

class ImageType(models.Model):
    name = models.CharField(max_length=20)


class Gallery(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    upload_date = models.DateField(auto_now_add=True)
    background = models.ForeignKey(Background, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image_type = models.ForeignKey(ImageType, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True)


