from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.services.jwt_service import JwtService


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtService.validate_activate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs.get('token')
        new_password = self.request.data.get('new_password')

        if not new_password:
            return Response({'new_password': 'this field is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = JwtService.validate_recovery_password_token(token)
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_200_OK)
