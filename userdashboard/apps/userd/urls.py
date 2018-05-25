from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', views.login),
    url(r'^log_in$', views.log_in),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/admin$', views.admin),
    url(r'^registration$', views.registration),
    url(r'^register$', views.register),
    url(r'^users/show/(?P<id>\d+)$', views.userboard),
    url(r'^message/(?P<id>\d+)$', views.msg),
    url(r'^users/show/message/(?P<id>\d+)$', views.msg),
    url(r'^comment/(?P<id>\d+)$', views.comments),
    
]