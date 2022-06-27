from django.urls import path

from .views import ListCreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('/<int:pk>', RetrieveUpdateDestroyView.as_view())
]
