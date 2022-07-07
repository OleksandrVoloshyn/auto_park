from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from permissions.user_permissions import IsSuperUser

from .serializers import AddAvatarSerializer, UserSerializer, UserStaffSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class AddAvatarView(UpdateAPIView):
    http_method_names = ('patch',)
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile


class UserToAdminUpdateView(UpdateAPIView):
    http_method_names = ('patch',)
    serializer_class = UserStaffSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def perform_update(self, serializer):
        candidate = self.get_object()
        serializer.save(is_staff=True)


class AdminToUserUpdateView(UserToAdminUpdateView):
    def perform_update(self, serializer):
        candidate = self.get_object()
        serializer.save(is_staff=False)
