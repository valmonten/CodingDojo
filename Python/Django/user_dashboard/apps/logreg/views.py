# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request, 'logreg/sign_in.html')
def register(request):
    return render(request, 'logreg/register.html')
def home(request):
    return render(request, 'logreg/home.html')