from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import CarSerializer
from .models import CarModel


class CarCreatedView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return CarModel.objects.filter(user=self.request.user)
