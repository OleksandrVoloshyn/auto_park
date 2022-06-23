from django.urls import path

from users.views import UsersListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users', UsersListCreateView.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view())
]
