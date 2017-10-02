# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.


class UsersManager(models.Manager):
    def register_valid(self, d):
        errors={}
        if d['password']!=d['pw_conf']:
            errors['password'] = 'Passwords do not match'
        if not re.match("^[A-Za-z ]*$", d['name']):
            errors['name'] = "Name can only contain letters"
        try:
            trying = Users.objects.get(email=d['email'])
            errors['email'] = "Email already in use"
        except Users.DoesNotExist:
            pass
        return errors

    def login_valid(self, d):
        em = d['email']
        pw = d['password']

        errors = {}

        try:
            trying = Users.objects.get(email = em).pw
        except Users.DoesNotExist:
            errors['email'] = "Email password combo does not exist"
            return errors
        
        
        if bcrypt.checkpw(pw.encode(), trying.encode()):
            pass
        else:
            errors['password'] = "Email password combo does not exist"
        return errors

class Users(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()

        

            