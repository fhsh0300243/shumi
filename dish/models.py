from django.db import models

# Create your models here.
from django.utils import timezone

class DishPost(models.Model):
    DishTitle=models.CharField(max_length=200)
    DishContent=models.TextField(blank=True)
    DishPhoto=models.URLField(blank=True)
    DishCreated_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.DishTitle