from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView

from .models import AutoParksModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarCreateSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParksModel.objects
    serializer_class = CarCreateSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park_id=auto_park.id)


class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects
    serializer_class = AutoParkSerializer
