from django.contrib import admin

# Register your models here.
from .models import Dish_post, Dish_comment, Dish_comment_reply

admin.site.register(Dish_post)
admin.site.register(Dish_comment)
admin.site.register(Dish_comment_reply)