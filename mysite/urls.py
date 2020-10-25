from django.contrib import admin
from django.urls import path, include
from myweb import views
#from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('Login', views.Login , name ='login'),
    path('Logout/', views.Logout),
    path('Register', views.Register),
    #path('polls/', include('polls.urls')),
    path('myweb/',include('myweb.urls')),
    path('admin/', admin.site.urls),
    path('anime/', views.anime),
    path('anime1/', views.anime1),
    path('anime2/', views.anime2),
    path('insertmovie/', views.insertmovie),
]
