from django.urls import path, include
from .views import (HomeView, CheckOutView, EmployeeView,CheckOutTemplateView, AttendanceView,
                    CheckInView,EmployeeProfileView,AttendanceTemplateView)

urlpatterns = [
path('', HomeView.as_view()),
path('employee_profile/', EmployeeView.as_view()),
path('employee_profile_api/', EmployeeProfileView.as_view()),
path('attendance_api/', AttendanceView.as_view()),
path('attendance/', AttendanceTemplateView.as_view()),
path('checkin_api/', CheckInView.as_view()),
path('checkout/', CheckOutTemplateView.as_view()),
path('checkout_api/', CheckOutView.as_view()),

]
