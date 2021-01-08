from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('work/',views.work,name="work"),
    path('team/',views.team,name="team"),
    path('join/',views.join,name="join"),
    path('login/',views.loginpage,name='login'),
    path('accounts/login/',RedirectView.as_view(url='/login/', permanent=False)),
    path('logout/',LogoutView.as_view(next_page="/"),name='logout'),
    path('management/',views.management,name='management'),
]
