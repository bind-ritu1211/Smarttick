from django.urls import path,include
from .views import HomeView,CheckInView,CheckOutView,EmployeeView,AttendanceView

urlpatterns = [
    path('index/', HomeView.as_view()),
    path('checkin/', CheckInView.as_view()),
    path('checkout/', CheckOutView.as_view()),
    path('employee_profile/', EmployeeView.as_view()),
    path('attendance/', AttendanceView.as_view()),

]