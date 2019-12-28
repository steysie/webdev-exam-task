# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length = 88)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
