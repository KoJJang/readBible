from django import forms

from .models import Script

class PostForm(forms.ModelForm):

    class Meta:
        model = Script
        fields = ('title', 'text',)