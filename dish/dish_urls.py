from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.dish_home, name='dish_list'),
    url(r'^(?P<pk>\d+)/$', views.dish_detail, name='dish_detail'),
]