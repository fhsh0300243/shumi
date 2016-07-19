from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.dish_home, name='dish_list'),
    url(r'^(?P<pk>\d+)/$', views.dish_detail, name='dish_detail'),
    url(r'^new/$', views.dish_new, name='dish_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.dish_edit, name='dish_edit'),
]