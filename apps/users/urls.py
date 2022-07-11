from django.urls import path

from .views import AddAvatarView, AdminToUserView, RecoveryPasswordView, UserListCreateView, UserToAdminView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),
    path('/recovery_password', RecoveryPasswordView.as_view())
]
