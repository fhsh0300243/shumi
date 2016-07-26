from django import forms
from .models import Dish_post, Dish_comment, Dish_comment_reply

class DishPostForm(forms.ModelForm):

    class Meta:
        model=Dish_post
        fields=('Dish_title', 'Dish_content', 'Dish_photo',)

class DishCommentForm(forms.ModelForm):

    class Meta:
        model = Dish_comment
        fields=('Your_name', 'Content',)

class DishCommentReplyForm(forms.ModelForm):

    class Meta:
        model = Dish_comment_reply
        fields=('Your_name', 'Content',)