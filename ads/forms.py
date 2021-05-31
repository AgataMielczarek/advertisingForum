from django import forms
from django.forms import fields
from .models import Advertisement

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        #fields = ('company', 'address')
        exclude = ('user',)