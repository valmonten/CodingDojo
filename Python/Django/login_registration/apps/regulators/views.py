# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    context = {
        "Reg": Reg,
        "Log": Log,
    }
    return render(request, 'regulators/index.html', context)
def show(request):

    return render(request, 'regulators/show.html')
def log(request):
    login_valid(request.POST)
    context = {
        "name":
        "from":
    }
    return redirect('/success')
def reg(request):
    errors = Users.objects.users_valid(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())

        Users.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], pw=hash1)
    return redirect('/success')