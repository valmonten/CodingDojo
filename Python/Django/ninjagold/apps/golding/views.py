# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random, time

import pygame
from pygame.locals import *

pygame.init()
# Create your views here.
def index(request):
    if not request.session.get('gold'):
        request.session['gold']=0
    if not request.session.get('activity'):
        request.session['activity']=[]
    return render(request, 'golding/index.html')

def farm(request):
    rando=random.randint(10,20)
    request.session['gold']+=rando
    request.session['activity'].append("You earned "+str(rando)+" gold from the farm! on "+time.strftime('%c'))
    
    return redirect('/')

def cave(request):
    rando=random.randint(5,10)
    request.session['gold']+=rando
    request.session['activity'].append("You earned "+str(rando)+" gold from the cave! on "+time.strftime('%c'))
    return redirect('/')

def house(request):
    rando=random.randint(2,5)
    request.session['gold']+=rando
    request.session['activity'].append("You earned "+str(rando)+" gold from the house! on "+time.strftime('%c'))
    return redirect('/')

def casino(request):
    rando=random.randint(-50,50)
    request.session['gold']+=rando
    request.session['activity'].append("You earned "+str(rando)+" gold from the casino! on "+time.strftime('%c'))
    return redirect('/')

