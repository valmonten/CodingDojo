from django import forms

class Theform(forms.Form):
    first = forms.CharField(label="First name", max_length=100)
    email = forms.EmailField(label="email", max_length=100)


