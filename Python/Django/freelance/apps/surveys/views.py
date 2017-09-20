# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def show(request):
    return HttpResponse('Placeholder to show all surveys')
def new(request):
    return HttpResponse('Placeholder for new surveys')