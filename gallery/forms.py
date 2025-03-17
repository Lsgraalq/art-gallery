from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Artist, Painting
from .models import Artist
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Artist, Painting
# Форма для редактирования картины в админке
class PaintingAdminForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'auction', 'author', 'price', 'is_for_sale']  # Можно добавить другие поля, если нужно

    auction = forms.BooleanField(required=False, label='Выставлено на аукцион', widget=forms.CheckboxInput())


class ArtistRegisterForm(UserCreationForm):
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Artist
        fields = ['username', 'email', 'bio', 'password1', 'password2']

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'text', 'image', 'auction', 'width', 'height', 'paint_type', 'canvas_material', 'is_for_sale', 'price', 'year_of_creation']
        
        # Опциональные поля могут быть определены как пустые, если не требуется валидация для них
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'paint_type': forms.TextInput(attrs={'class': 'form-control'}),
            'canvas_material': forms.TextInput(attrs={'class': 'form-control'}),
            'is_for_sale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_of_creation': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    # Добавление кастомных валидаций, если нужно
    def clean_price(self):
        price = self.cleaned_data.get('price')
        is_for_sale = self.cleaned_data.get('is_for_sale')
        
        if is_for_sale and not price:
            raise forms.ValidationError("Если картина продается, цена обязательно должна быть указана.")
        return price




class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['bio', 'profile_pic','first_name','last_name']  # Поля для редактирования профиля
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),  # Виджет для textarea
        }
        