# blog/forms.py

from django import forms
from . import models


class SheetForm(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = [
            'process',
            'defect',
            'period',
            'coorx',
            'coory',
        ]
        widgets = {
            'coorx': forms.HiddenInput(),
            'coory': forms.HiddenInput(),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }

class AjaxImageForm(forms.ModelForm):
    class Meta:
        model = models.AjaxImage
        fields = ['image_coord']
