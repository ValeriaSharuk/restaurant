from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import AboutInfo, FeedbackInfo


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 100)


class AboutForm(ModelForm):
    class Meta:
        model = AboutInfo
        fields = ['title', 'full_text']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Информация о компании'}),
        }


class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackInfo
        fields = ['full_name', 'full_text', 'image']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
        }
