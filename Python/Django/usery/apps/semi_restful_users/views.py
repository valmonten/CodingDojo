# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'semi_restful_users/index.html')
def show(request):
    return render(request, 'semi_restful_users/show.html')
def add(request):
    return render(request, 'semi_restful_users/add.html')