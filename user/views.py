from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import UserModel


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().exclude(id=self.request.user.id)
        return Response(UserSerializer(qs, many=True).data)


class GetCurrentUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        data = UserSerializer(user).data
        return Response(data)
