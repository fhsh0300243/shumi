from django.db import models

# Create your models here.
from django.utils import timezone
from hitcount.models import HitCountMixin

class Life_post(models.Model, HitCountMixin):
    Life_title=models.CharField(max_length=200)
    Life_content=models.TextField(blank=True)
    Life_photo=models.URLField(blank=True)
    Life_post_created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Life_title

class Life_comment(models.Model):
    Life_comment_post=models.ForeignKey('Life_post', related_name='comments')
    Your_name=models.CharField(max_length=200)
    Content=models.TextField()
    Life_comment_created_date=models.DateField(default=timezone.now)
    Life_comment_approved=models.BooleanField(default=False)

    def approve(self):
        self.Life_comment_approved=True
        self.save()

    def __str__(self):
        return self.Content

    def Life_approved_comments(self):
        return self.Life_comment.filter(Life_comment_approved=True)

class Life_comment_reply(models.Model):
    Life_comment_reply_post=models.ForeignKey('Life_comment', related_name='replies', null=True)
    Your_name=models.CharField(max_length=200, default='業障研發工程師')
    Content=models.TextField()
    Life_comment_reply_created_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.Content