from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects
    serializer_class = CarSerializer

    def get_queryset(self):
        auto_park_id = self.request.query_params.get('autoParkId')
        if auto_park_id:
            return self.queryset.filter(auto_park_id=auto_park_id)
        return super().get_queryset()


class CarUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects
    serializer_class = CarSerializer
