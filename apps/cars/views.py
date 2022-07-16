from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)
    filterset_class = CarFilter


class CarUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get a Car
    put:
        Update car
    delete:
        Delete car
    """
    queryset = CarModel.objects
    serializer_class = CarSerializer
