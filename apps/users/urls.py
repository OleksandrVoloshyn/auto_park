from django.urls import path

from .views import AddAvatarView, ToUsualUserUpdateView, UserListCreateView, UserToAdminUpdateView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminUpdateView.as_view()),
    path('/<int:pk>/remove_admin', ToUsualUserUpdateView.as_view())
]
