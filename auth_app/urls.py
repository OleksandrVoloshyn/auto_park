from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import RegisterView, CustomTokenRefreshView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('refresh/', CustomTokenRefreshView.as_view()),
    path('register/', RegisterView.as_view())
]
