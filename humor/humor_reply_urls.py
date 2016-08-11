from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^(?P<pk2>\d+)/reply/$', views.humor_add_reply_to_comment, name='humor_add_reply_to_comment'),
    ]