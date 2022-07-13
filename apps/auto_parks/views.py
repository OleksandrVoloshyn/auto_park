from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.cars.serializers import CarCreateSerializer

from .filters import AutoParkFilter
from .models import AutoParksModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = AutoParkFilter


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
