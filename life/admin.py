from django.contrib import admin

# Register your models here.
from .models import Life_post, Life_comment, Life_comment_reply

admin.site.register(Life_post)
admin.site.register(Life_comment)
admin.site.register(Life_comment_reply)