from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.dish_home, name='dish_list'),
    url(r'^(?P<pk>\d+)/$', views.dish_detail, name='dish_detail'),
    url(r'^new/$', views.dish_new, name='dish_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.dish_edit, name='dish_edit'),
    url(r'^(?P<pk>\d+)/comment/$', views.dish_add_comment_to_post, name='dish_add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.dish_comment_approve, name='dish_comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.dish_comment_remove, name='dish_comment_remove'),
    url(r'^(?P<pk1>\d+)/comment/', include('dish.dish_reply_urls')),
]