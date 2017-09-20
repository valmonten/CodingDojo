# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not request.session.get('counter'):
        request.session['counter']=0
    request.session['counter']+=1
    request.session['word']= get_random_string(length=14)

    return render(request, 'wordgen/index.html')
def reset(request):
    del request.session['counter']
    return redirect('/random_word/')
def generate(request):
    
    
    return redirect('/random_word/')