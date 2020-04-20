from django.shortcuts import render
from django .views .generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


class CheckInView(TemplateView):
    template_name = "checkin.html"


class CheckOutView(TemplateView):
    template_name = "checkout.html"


class EmployeeView(TemplateView):
    template_name = "employee_profile.html"
  

class AttendanceView(TemplateView):
    template_name = "attendance.html"