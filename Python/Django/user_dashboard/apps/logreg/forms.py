from django import forms

class Sign_in_forms(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

class Register_forms(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    pwconf = forms.CharField(widget=forms.PasswordInput, pwconf=password)
