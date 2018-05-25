from django.conf.urls import url 
from . import views 
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.staticfiles

urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^amadon/buy$', views.buy),
]