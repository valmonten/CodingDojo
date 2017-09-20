# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "blogs/index.html")
def new(request):
    return HttpResponse("Placeholder for new form to create blogs")
def create(request):
    return redirect('/blogs/')
def show(request, number):
    return HttpResponse("Placeholder for blog number " + number)
def edit(request, number):
    return HttpResponse('Placeholder to edit blog number ' + number)
def destroy(request, number):
    return redirect('/blogs')