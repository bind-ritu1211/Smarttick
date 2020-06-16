from django.utils.decorators import method_decorator
from django.shortcuts import render
from django .views .generic import TemplateView
from rest_framework.views import APIView
from .models import EmployeeProfile,Attendance
from rest_framework.response import Response
from .serializer import EmployeeProfileSerializer,AttendanceSerializer
from datetime import datetime
from django.contrib.auth.decorators import login_required
import datetime
datetime.date.today()
import _datetime
now = datetime.datetime.now()
today = _datetime.date.today()
print(today)
current_time = now.strftime("%H:%M")
# Create your views here.


class HomeView(TemplateView):
    template_name = "common/checkin.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})



class AttendanceTemplateView(TemplateView):
    template_name = "common/attendance.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})


class AttendanceView(APIView):
    def get(self, request, format=None):
        attendance = Attendance.objects.filter(employee_profile=self.request.user)
        attendance = AttendanceSerializer(attendance, many=True)
        return Response(attendance).data




class CheckOutTemplateView(TemplateView):
    template_name = "common/checkout.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})



class CheckInView(APIView):
    def post(self, request, *args):
        is_availble_employee = Attendance.objects.filter(employee_profile=self.request.user)
        if not is_availble_employee:
            if current_time == "10:00" or current_time < "10:30":
                attendance = Attendance.objects.create(status="Full_Day",
                                                employee_profile=self.request.user,
                                                check_in= now,
)
            else:
            #pass
                attendance= Attendance.objects.create(status="Half_Day",
                                                employee_profile=self.request.user,
                                                check_in= now,
)
            return Response("successfully checked in")
        else:
            return Response("already checked in")




class CheckOutView(APIView):
    def post(self, request, *args):
        attendance = Attendance.objects.filter(employee_profile=self.request.user)
        if attendance:
            #pass
            attendance.update(check_out= now )
        return Response("successfully check out") 
        #print("successfully check out")



class EmployeeView(TemplateView):
    template_name = "common/employee_profile.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, self.template_name, {})
        



class EmployeeProfileView(APIView):
    def get(self, request, format=None):
        employee_profile = EmployeeProfile.objects.filter(user=self.request.user)
        employee_profile = EmployeeProfileSerializer(employee_profile, many=True)
        return Response(employee_profile.data)