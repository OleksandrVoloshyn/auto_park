from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions.user_permissions import IsSuperUser

from .serializers import AddAvatarSerializer, UserSerializer

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


class UserToAdminView(GenericAPIView):
    http_method_names = ('patch',)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        candidate = self.get_object()

        if not candidate.is_staff:
            candidate.is_staff = True
            candidate.save()

        serializer = self.serializer_class(candidate)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(UserToAdminView):
    def patch(self, *args, **kwargs):
        candidate = self.get_object()

        if candidate.is_staff:
            candidate.is_staff = False
            candidate.save()

        serializer = self.serializer_class(candidate)
        return Response(serializer.data, status.HTTP_200_OK)
