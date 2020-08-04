
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("enrollUser", views.enrollUser, name="enrollUser"),
    #path("createMeetup", views.createMeetup, name="createMeetup"),
    #API Routes
    path("profile", views.profile, name="profile"),
    path("meetups", views.meetups, name="meetups"),
    path("enrolled", views.enrolled, name="enrolled"),
  #  path("map", views.register, name="map"),
]
