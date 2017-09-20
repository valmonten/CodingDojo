# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hey!')

def dog(request):
    return render(request, 'fly/plane.html')