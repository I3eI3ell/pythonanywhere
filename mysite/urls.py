from django.contrib import admin
from django.urls import path, include
from myweb import views
#from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('Login', views.Login),
    path('Register', views.Register),
    #path('polls/', include('polls.urls')),
    path('myweb/',include('myweb.urls')),
    path('admin/', admin.site.urls),
    path('anime/', views.anime),
    path('ThaiDubbing/', views.ThaiDubbing),
]
