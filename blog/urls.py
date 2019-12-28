"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog import views
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "My Blog"
    description = "For Web Dev exam task and beyond"
    link = "/blog/feed/"
    
    def items(self):
        return Post.objects.all().order_by("-created")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return u"/blog/%d" % item.id


urlpatterns = [
    url(r'^$', ListView.as_view(
            queryset=Post.objects.all().order_by("-created")[:5],
            template_name = "blog.html")),
    url(r'^(?P<pk>\d+)', DetailView.as_view(
            model=Post,
            template_name = "post.html")),
    url(r'^archives/$', ListView.as_view(
            queryset=Post.objects.all().order_by("-created"),
            template_name = "archives.html")),
    url(r'^tag/(?P<tag>\w+)$', views.tagpage, name='tagpage'),
    url(r'^feed/$', BlogFeed())
]
