from django.conf.urls import url 
from . import views 
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.staticfiles

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add$',views.add),
    url(r'^clear$',views.clear),
]