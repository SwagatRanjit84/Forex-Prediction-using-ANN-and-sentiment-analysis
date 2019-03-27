from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user1$', views.index, name='index'),

    url(r'^admin1$', views.crawlera, name='crawlera'),
    url(r'^admin$', views.traina, name='traina'),
    url(r'^abc$', views.abca, name='abca'),

]

