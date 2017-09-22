from django import forms

class Reg(forms.Form):
    fname = forms.CharField(label="First name", max_length=50, min_length=2)
    lname = forms.CharField(label="Last name", max_length=50, min_length=2)
    email = forms.EmailField(label="Email", max_length=50)
    pw = forms.CharField(label="Passweird" , widget = forms.PasswordInput(), min_length = 8)
    confpw = forms.CharField(label="Confirm Passweird",widget = forms.PasswordInput())
    


class Log(forms.Form):
    email = forms.EmailField(max_length=50)
    pw = forms.CharField(label="Passwiord", widget = forms.PasswordInput(), min_length = 8)