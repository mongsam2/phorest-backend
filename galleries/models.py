from django.db import models

# Create your models here.
class Background(models.Model):
    image = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    recommend = models.BooleanField(default=False)

class ImageType(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Gallery(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    upload_date = models.DateField(auto_now_add=True)
    background = models.ForeignKey(Background, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image_type = models.ForeignKey(ImageType, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="galleries")
    # ManyToMany
    like_users = models.ManyToManyField('users.User', through='users.UserGallery', related_name="liking_galleries")


