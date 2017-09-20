# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import Theform

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html',{"form": Theform})
def process(request):
    print request.POST['first']    
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comments']=request.POST['comments']
    return redirect('/results')
def results(request):

    return render(request, 'surveys/results.html')
def back(request):
    return redirect('/')