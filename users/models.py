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
    