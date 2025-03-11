from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Artist

class ArtistRegisterForm(UserCreationForm):
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Artist
        fields = ['username', 'email', 'bio', 'password1', 'password2']
