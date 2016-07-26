from django.db import models

# Create your models here.
from django.utils import timezone
from hitcount.models import HitCountMixin

class Dish_post(models.Model, HitCountMixin):
    Dish_title=models.CharField(max_length=200)
    Dish_content=models.TextField(blank=True)
    Dish_photo=models.URLField(blank=True)
    Dish_post_created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Dish_title

class Dish_comment(models.Model):
    Dish_comment_post=models.ForeignKey('Dish_post', related_name='comments')
    Your_name=models.CharField(max_length=200)
    Content=models.TextField()
    Dish_comment_created_date=models.DateField(default=timezone.now)
    Dish_comment_approved=models.BooleanField(default=False)

    def approve(self):
        self.Dish_comment_approved=True
        self.save()

    def __str__(self):
        return self.Content

    def Dish_approved_comments(self):
        return self.Dish_comment.filter(Dish_comment_approved=True)

class Dish_comment_reply(models.Model):
    Dish_comment_reply_post=models.ForeignKey('Dish_comment', related_name='replies', null=True)
    Your_name=models.CharField(max_length=200, default='業障研發工程師')
    Content=models.TextField()
    Dish_comment_reply_created_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.Content