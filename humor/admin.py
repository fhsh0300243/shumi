from django.contrib import admin

# Register your models here.
from .models import Humor_post, Humor_comment, Humor_comment_reply

admin.site.register(Humor_post)
admin.site.register(Humor_comment)
admin.site.register(Humor_comment_reply)