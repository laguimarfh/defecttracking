# blog/forms.py

from django import forms
from . import models

class NameForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)


class ExampleSignupForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField()
    gender = forms.ChoiceField(
        label='Gender',
        required=False,
        choices=[
            (None, '-------'),
            ('m', 'Male'),
            ('f', 'Female'),
            ('n', 'Non-binary'),
        ]
    )
    receive_newsletter = forms.BooleanField(
        required=False,
        label='Do you wish to receive our newsletter?'
    )

class PhotoContestForm(forms.Form):
    name = forms.CharField(label='Full name', max_length=50)
    email = forms.EmailField()
    photo = forms.ImageField()

class SheetForm(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = [
            'process',
            'defect',
            'period',
            'location',
        ]
        