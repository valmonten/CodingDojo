from django import forms
from django.forms import widgets
class Register(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    alias = forms.CharField(label="Alias", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    pw_conf = forms.CharField(min_length=8, label='Confirm Passwird', widget = forms.PasswordInput)