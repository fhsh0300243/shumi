from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.humor_home, name='humor_list'),
    url(r'^(?P<pk>\d+)/$', views.humor_detail, name='humor_detail'),
    url(r'^new/$', views.humor_new, name='humor_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.humor_edit, name='humor_edit'),
    url(r'^(?P<pk>\d+)/comment/$', views.humor_add_comment_to_post, name='humor_add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.humor_comment_approve, name='humor_comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.humor_comment_remove, name='humor_comment_remove'),
    url(r'^(?P<pk1>\d+)/comment/', include('humor.humor_reply_urls')),
]