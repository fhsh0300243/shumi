from django import forms
from .models import DishPost

class DishPostForm(forms.ModelForm):

    class Meta:
        model=DishPost
        fields=('DishTitle', 'DishContent', 'DishPhoto',)