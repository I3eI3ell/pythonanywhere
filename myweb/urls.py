from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('',views.Login, name="Login"),
    path('',views.Register, name="Register"),
    path('', views.anime, name='anime'),
    path('', views.ThaiDubbing, name='ThaiDubbing'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
