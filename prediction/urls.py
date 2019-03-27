from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^user$', views.index, name='index'),
    url(r'^admin1$', views.crawler, name='crawler'),
    url(r'^admin$', views.train, name='train'),
    url(r'^abc$', views.abc, name='abc'),


]

