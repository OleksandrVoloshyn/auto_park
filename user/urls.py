from django.urls import path

from .views import UserListView, GetCurrentUserView

urlpatterns = [
    path('', UserListView.as_view()),
    path('current/', GetCurrentUserView.as_view())
]
