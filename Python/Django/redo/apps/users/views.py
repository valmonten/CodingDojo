# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def register(response):
    return HttpResponse('Placeholder for registering')
def login(response):
    return HttpResponse('Placeholder for loging in')
def users(response):
    print "something"
    return HttpResponse('Placeholder for usersing')

