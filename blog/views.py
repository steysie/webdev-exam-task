# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from blog.models import Post

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts":posts, "tag":tag})

