from django.contrib.auth.models import User
from django import forms
from . import models


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("The two password fields must match.")
        return cleaned_data


class LinkModelForm(forms.ModelForm):
    author = forms.Field(widget=forms.HiddenInput)

    class Meta:
        model = models.Link
        fields = ['url', 'name', 'author']
