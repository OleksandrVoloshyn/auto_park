from django.contrib import admin
from django.urls import path

from users.views import UsersListCreateView

urlpatterns = [
    path('users', UsersListCreateView.as_view()),
]
