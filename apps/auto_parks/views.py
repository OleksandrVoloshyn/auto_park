from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView

from apps.cars.serializers import CarCreateSerializer

from .models import AutoParksModel
from .serializers import AutoParkSerializer


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
