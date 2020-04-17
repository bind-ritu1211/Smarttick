from django.urls import path,include
from .views import HomeView

urlpatterns = [
    path('index/', HomeView.as_view()),
    
]