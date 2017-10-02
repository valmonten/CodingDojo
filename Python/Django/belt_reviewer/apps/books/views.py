# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    print Add_Book
    context = {
        "form": Add_Book
    }
    return render(request, 'books/index.html', context)
