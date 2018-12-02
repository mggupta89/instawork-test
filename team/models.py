# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from exceptions import InstaworkException



class Team(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.TextField() #should add a validator
    role = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.role not in settings.INSTA_ROLES:
            raise InstaworkException('Invalid role')
            pass
        super(Team, self).save(*args, **kwargs)

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'role': self.role
        }


