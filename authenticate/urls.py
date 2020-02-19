from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('unlock/', views.unlock, name="unlock"),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
