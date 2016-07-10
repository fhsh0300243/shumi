from django.db import models

# Create your models here.
from django.utils import timezone

class LifePost(models.Model):
    LifeTitle=models.CharField(max_length=200)
    LifeContent=models.TextField(blank=True)
    LifePhoto=models.URLField(blank=True)
    LifeCreated_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.LifeTitle