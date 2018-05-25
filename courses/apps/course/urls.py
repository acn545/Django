from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy$', views.confirm_GET),
    url(r'^delete$', views.delete),
    url(r'^courses/destroy/\d$', views.confirm_POST),
    url(r'^add$', views.add),
]