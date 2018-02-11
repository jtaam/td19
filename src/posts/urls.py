from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]

# from . import views
# urlpatterns = [
#     url(r'^$', "posts.views.post_list"),
#     url(r'^create/$', "posts.views.post_create"),
#     url(r'^detail/$', "posts.views.post_detail"),
#     url(r'^update/$', "posts.views.post_update"),
#     url(r'^delete/$', "posts.views.post_delete"),
#     # url(r'^posts/$', "<appname>.views.<function_name>"),
# ]
