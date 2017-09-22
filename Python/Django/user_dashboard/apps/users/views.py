# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, 'users/index.html')
    
def show(request, name):
    return render(request, 'users/show.html',{"name":name})