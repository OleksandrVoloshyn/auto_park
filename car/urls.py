from django.urls import path

from .views import CarCreatedView

urlpatterns = [
    path('', CarCreatedView.as_view())
]
