from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.life_home, name='life_list'),
    url(r'^(?P<pk>\d+)/$', views.life_detail, name='life_detail'),
]