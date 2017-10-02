# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
import bcrypt

# Create your views here.
def session_setter(request):
    rp = request.POST
    request.session['name'] = rp['name']
    request.session['alias'] = rp['alias']
    em = rp['email']
    request.session['email'] = em
    request.session ['id'] = Users.objects.get(email=em).id

def index(request):
    context = {
        'reg':Register
    }
    return render(request, 'logreg/index.html', context)

def register_process(request):
    errors = Users.objects.register_valid(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error, extra_tags=tag)
        return redirect('/')
    else:
        rp = request.POST
        hashed = bcrypt.hashpw(rp['password'].encode(), bcrypt.gensalt())
        Users.objects.create(name=rp['name'], alias=rp['alias'], email=rp['email'], password=hashed)

    session_setter(request)

    return redirect('/books')

def login_process(request):
    errors = Users.objects.login_valid(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    session_setter(request)

    return redirect('/books')
