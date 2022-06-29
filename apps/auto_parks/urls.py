from django.urls import path

from .views import AutoParkListCreateView, AutoParkAddCarView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view())
]
