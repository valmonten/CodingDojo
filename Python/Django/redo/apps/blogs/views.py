# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(response):
    return HttpResponse('Placeholder for blogs')
def new(response):
    return HttpResponse("Placeholder for creating new blog")
def create(response):
    return redirect('/blogs')
def show(response, number):
    return HttpResponse('Placeholder for blog number '+number)
def edit(response, number):
    return HttpResponse('Placeholder for editing blog ' +number)
def destroy(response, number):
    return redirect('/blogs')

