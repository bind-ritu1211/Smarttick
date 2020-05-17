from django.shortcuts import render
from django .views .generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class HomeView(TemplateView):
    template_name = "common/checkin.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})


class CheckOutView(TemplateView):
    template_name = "common/checkout.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})


class EmployeeView(TemplateView):
    template_name = "common/employee_profile.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})


class AttendanceView(TemplateView):
    template_name = "common/attendance.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})
