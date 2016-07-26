from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.life_home, name='life_list'),
    url(r'^(?P<pk>\d+)/$', views.life_detail, name='life_detail'),
    url(r'^new/$', views.life_new, name='life_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.life_edit, name='life_edit'),
    url(r'^(?P<pk>\d+)/comment/$', views.life_add_comment_to_post, name='life_add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.life_comment_approve, name='life_comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.life_comment_remove, name='life_comment_remove'),
    url(r'^(?P<pk1>\d+)/comment/', include('life.life_reply_urls')),
]