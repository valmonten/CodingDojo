# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def show(request):
    
    return render(request, 'button/win.html')

def go(request):
    
    return redirect('/')