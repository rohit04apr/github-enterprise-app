from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls')),

    #url(r'^oauth/', include('social_django.urls', namespace='social')),
]
