from django.forms import ModelForm
from django import forms
from .models import User, Wallet


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=10, widget=forms.HiddenInput(), required=False)


class New_User(MultipleForm, ModelForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class New_Wallet(MultipleForm, ModelForm):
    class Meta:
        model = Wallet
        fields = ('wallet',)
