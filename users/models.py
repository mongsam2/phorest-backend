from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class LoginPathChoices(models.TextChoices):
        KAKAO = ("kakao", "카카오")
        GOOGLE = ("google", "구글")
        NAVER = ("naver", "네이버")
        LOCAL = ("local", "기본")

    #Abstractuser 
    #-------------------------------
    #username
    #email
    #password
    #-------------------------------
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    profile_image = models.ImageField()
    login_path = models.CharField(max_length=6, choices=LoginPathChoices.choices)
    is_email_subscribed = models.BooleanField(default=False)
    # ManyToMany
    products = models.ManyToManyField('products.Product', through='UserProduct', related_name="users")
    
    
class UserGallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery = models.ForeignKey('galleries.Gallery', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class UserProduct(models.Model):

    class DeliveryChoices(models.TextChoices):
        COMPLETE = ("complete", "배송완료")
        PROGRESS = ("progress", "배송중")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_delivered = models.CharField(max_length=8, choices=DeliveryChoices.choices)
    count = models.PositiveIntegerField(default=0)