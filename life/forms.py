from django import forms
from .models import Life_post, Life_comment, Life_comment_reply

class LifePostForm(forms.ModelForm):

    class Meta:
        model=Life_post
        fields=('Life_title', 'Life_content', 'Life_photo',)

class LifeCommentForm(forms.ModelForm):

    class Meta:
        model = Life_comment
        fields=('Your_name', 'Content',)

class LifeCommentReplyForm(forms.ModelForm):

    class Meta:
        model = Life_comment_reply
        fields=('Your_name', 'Content',)