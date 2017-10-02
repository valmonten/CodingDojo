# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import resolve
from views import LandingView

# Create your tests here.
class TripTest(TestCase):
    """Test that landing view is stufff!"""
    def test_landing_endpoint(self):
        endpoint = resolve('/')
        
        self.asserEquals(endpoint.func, landing)
# def landing(request):
#     """Takes us to logreg"""
#     context = {}

