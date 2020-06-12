from django.urls import path, include
from .views import HomeView, CheckOutView, EmployeeView, AttendanceView,CheckInView,EmployeeProfileView

urlpatterns = [
path('', HomeView.as_view()),
path('checkout/', CheckOutView.as_view()),
path('checkin/', CheckInView.as_view()),
path('employee_profile/', EmployeeView.as_view()),
path('attendance/', AttendanceView.as_view()),
path('profile/', EmployeeProfileView.as_view()),

]
