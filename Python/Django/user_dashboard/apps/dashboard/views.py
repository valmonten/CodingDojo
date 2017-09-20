# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'dashboard/dashboard.html')

def dash(request):
    return render(request, 'dashboard/dashboard.html')