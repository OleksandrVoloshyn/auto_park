from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.cars.serializers import CarCreateSerializer

from .filters import AutoParkFilter
from .models import AutoParksModel
from .serializers import AutoParkSerializer

UserModel = get_user_model()


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = AutoParkFilter

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owners=[user])


class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParksModel.objects
    serializer_class = CarCreateSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park_id=auto_park.id)


class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects
    serializer_class = AutoParkSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


class AddOwnerToAutoParkView(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer

    def patch(self, *args, **kwargs):
        user = self.request.user
        auto_park = self.get_object()
        user_id = kwargs.get('user_id')
        new_owner = get_object_or_404(UserModel, pk=user_id)

        if auto_park.owners.filter(pk=user.id).exists():
            auto_park.owners.add(new_owner)
        # user.auto_parks.clear()
        # auto_park.owners.filter(id__lt=5).delete()

        return Response(self.get_serializer(auto_park).data, status=status.HTTP_200_OK)
