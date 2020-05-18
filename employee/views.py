
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django .views .generic import TemplateView
from rest_framework.views import APIView
from .models import EmployeeProfile,Attendance
from rest_framework.response import Response
from .serializer import EmployeeProfileSerializer,AttendanceSerializer
from datetime import datetime
from django.contrib.auth.decorators import login_required

now = datetime.now()
current_time = now.strftime("%H:%M")
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

class AttendanceView(APIView):

    def get(self, request, *args):
        attendance = Attendance.objects.all()
        attendance = AttendanceSerializer(attendance, many=True)
        return Response(attendance.data)


    def post(self, request, *args):
        check_in = request.POST.get('check_in')
        status = request.POST.get('status')
        employee_profile = request.POST.get('employee_profile')
        context = {}
        if current_time == "10:00" or  current_time < "10:30":
            attendance = Attendance.objects.create(status="Full_Day",
                                                   employee_profile=employee_profile,
                                                   check_in=check_in,
                                                  )
        context.update({
            "status": status,
            "check_in": check_in,
            "employee_profile": employee_profile,
           })
        print(context)
        return Response(context)    
           
class AttendanceView(APIView):
    def post(self, request, *arg, **kwrg):
        check_out = request.POST.get('check_out')
        employee_profile = request.POST.get('employee_profile')
        context = {}
        attendance = Attendance.objects.filter(employee_profile=employee_profile)
        if employee_profile :
                attendance = Attendance.objects.create(check_out=check_out)

        context.update({
        "check_out": check_out,
        })

        print(context)
        return Response(context)    


class EmployeeProfileView(APIView):
    def get(self, request, format=None):
        employee_profile = EmployeeProfile.objects.all()
        employee_profile = EmployeeProfileSerializer(employee_profile, many=True)
        return Response(employee_profile.data)
        

    #def post(self, request, *args, **kwargs):
     #   name = request.POST.get('name')
      #  email = request.POST.get('email')
       # address = request.POST.get('address')
        #city = request.POST.get('city')
        #state = request.POST.get('state')
       # gender = request.POST.get('gender')
        #designation = request.POST.get('designation')
       # age = request.POST.get('age')
      #  manager_name = request.POST.get('manager_name')
        #context = {}
       # employee_profile = EmployeeProfile.objects.create(name=name,
         #                              email=email,
          #                             address=address,
            #                           city=city,
           #                            state=state,
             #                          gender=gender,
              #                         designation=designation,
               #                        age=age,
                #                       manager_name=manager_name,
        #)
        #context.update({
         #   "name": name,
          #  "email": email,
           # "address": address,
            #"city": city,
            #"state": state,
            #"gender": gender,
            #"designation": designation,
            #"age": age,
            #"manager_name": manager_name,
        #})
        #print(context)
        #return Response(context)    
