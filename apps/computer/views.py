from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ComputerModel
from .serializers import ComputerSerializer


class ListCreateView(APIView):
    def get(self, *args, **kwargs):
        qs = ComputerModel.objects.all()
        serializer = ComputerSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ComputerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response({'err': 'Not Found'}, status.HTTP_404_NOT_FOUND)

        data = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response({'err': 'Not Found'}, status.HTTP_404_NOT_FOUND)

        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response({'err': 'Not Found'}, status.HTTP_404_NOT_FOUND)

        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response({'err': 'Not Found'}, status.HTTP_404_NOT_FOUND)

        computer = ComputerModel.objects.get(pk=pk)
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
