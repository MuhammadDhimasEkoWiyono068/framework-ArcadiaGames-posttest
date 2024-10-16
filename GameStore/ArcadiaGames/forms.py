# forms.py
from django import forms
from .models import Games

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['title', 'description', 'price', 'developer', 'release_date', 'image']
