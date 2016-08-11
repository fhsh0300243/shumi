from django.db import models

# Create your models here.
from django.utils import timezone
from hitcount.models import HitCountMixin
from embed_video.fields import EmbedVideoField

class Humor_post(models.Model, HitCountMixin):
    Humor_title=models.CharField(max_length=200)
    Humor_content=models.TextField(blank=True)
    Humor_video=EmbedVideoField()
    Humor_post_created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Humor_title

class Humor_comment(models.Model):
    Humor_comment_post=models.ForeignKey('Humor_post', related_name='comments')
    Your_name=models.CharField(max_length=200)
    Content=models.TextField()
    Humor_comment_created_date=models.DateField(default=timezone.now)
    Humor_comment_approved=models.BooleanField(default=False)

    def approve(self):
        self.Humor_comment_approved=True
        self.save()

    def __str__(self):
        return self.Content

    def Humor_approved_comments(self):
        return self.Humor_comment.filter(Humor_comment_approved=True)

class Humor_comment_reply(models.Model):
    Humor_comment_reply_post=models.ForeignKey('Humor_comment', related_name='replies', null=True)
    Your_name=models.CharField(max_length=200, default='業障研發工程師')
    Content=models.TextField()
    Humor_comment_reply_created_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.Content