from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/new$', views.add_user),
    url(r'^users/create$', views.create),
    url(r'^users/\d/edit$', views.edit),
    url(r'^users/\d/destroy$', views.destroy),
    url(r'^users/\d/update$', views.update),
    url(r'^users/\d$', views.show),
]