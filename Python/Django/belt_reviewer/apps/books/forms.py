
from django import forms
from .models import *

class Add_Book(forms.Form):
    title = forms.CharField(max_length=100)
    existing_author = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
    # new_author = 
    # review = 
    # rating = 

