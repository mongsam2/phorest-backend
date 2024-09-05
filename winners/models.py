from django.db import models

# Create your models here.
class Winner(models.Model):
    rank = models.PositiveIntegerField()
    win_date = models.DateField()
    weekly_like = models.PositiveIntegerField(default=0)
    gallery = models.ForeignKey('galleries.Gallery', on_delete=models.SET_NULL, null=True, blank=True)