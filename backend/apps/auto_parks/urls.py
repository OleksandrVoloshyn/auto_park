from django.urls import path

from .views import AddOwnerToAutoParkView, AutoParkAddCarView, AutoParkListCreateView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view()),
    path('/<int:pk>/add_owner/<int:user_id>', AddOwnerToAutoParkView.as_view()),
]
