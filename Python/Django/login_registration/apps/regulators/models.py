# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt


# Create your models here.
class UsersManager(models.Manager):
    def users_valid(self, postData):
        errors = {}
        if postData['pw'] != postData['confpw']:
            errors['pw'] = "Password must match Confirmation"
        if not re.match("^[A-Za-z]*$",postData['fname']):
            errors['fname'] = "First name can only contain letters"
        if not re.match("^[A-Za-z]*$",postData['lname']):
            errors['lname'] = "Last name can only contain letters"
        try: 
            trying = Users.objects.get(email=postData['email'])
            errors['email'] = "Email already in use"
        except Users.DoesNotExist:
            pass
        return errors
    def login_valid(self, postData):
        em = postData['email']
        paw = postData['pw']
        
        errors = {}
        try:
            trying = Users.objects.get(email=postData['email'])
        except Users.DoesNotExist:
            errors['email'] = "Email password combo does not exist"
            return errors
        a = Users.objects.get(email='em').pw 
        if bcrypt.checkpw(paw.encode(), a):
            request.session['log_id'] = Users.objects.get(email=em).id
        else:
            errors['password'] = "Email password combo does not exist"
        return errors                        



class Users(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()
