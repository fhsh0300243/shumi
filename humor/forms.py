from django import forms
from .models import Humor_post, Humor_comment, Humor_comment_reply

class HumorPostForm(forms.ModelForm):

    class Meta:
        model=Humor_post
        fields=('Humor_title', 'Humor_content', 'Humor_video',)

class HumorCommentForm(forms.ModelForm):

    class Meta:
        model = Humor_comment
        fields=('Your_name', 'Content',)

class HumorCommentReplyForm(forms.ModelForm):

    class Meta:
        model = Humor_comment_reply
        fields=('Your_name', 'Content',)