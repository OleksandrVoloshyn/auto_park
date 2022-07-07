from django.urls import path

from .views import AddAvatarView, AdminToUserUpdateView, UserListCreateView, UserToAdminUpdateView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminUpdateView.as_view()),
    path('/<int:pk>/remove_admin', AdminToUserUpdateView.as_view())
]
