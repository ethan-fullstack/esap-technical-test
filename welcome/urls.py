from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexView, name="index"),
    path("profile/", views.profileView, name="profile"),
    path("profile/<int:profile_id>/", views.profileDetailView, name="profile_detail"),
    path("list/", views.listView, name="list"),
]
