from django.urls import path
from django.conf.urls import include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('work',views.work,name="work"),
    path('team',views.team,name="team"),
    path('join',views.join,name="join"),
    path('login',views.login,name='login'),
]
