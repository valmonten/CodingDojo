# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..logreg.models import *

# Create your views here.
def admin(request):
    # context
    return render(request,'dashboard/dashboard.html')

def dash(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'dashboard/dashboard.html', context)