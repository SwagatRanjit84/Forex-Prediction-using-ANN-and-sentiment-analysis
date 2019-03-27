
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^prediction/', include('prediction.urls')),
    url(r'^backpropagation/', include('backpropagation.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
