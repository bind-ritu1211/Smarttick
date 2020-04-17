from django.urls import path,include
from .views import HomeView,CheckInView

urlpatterns = [
    path('index/', HomeView.as_view()),
    path('checkin/', CheckInView.as_view()),
   
]