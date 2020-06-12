from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
       return self.name
class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    SEX_CHOICE = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('BOTH', 'BOTH')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(choices=SEX_CHOICE,
                              max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    manager_name = models.CharField(max_length=255, blank=True, null=True)
    current_salary = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    user_image = models.ImageField(upload_to='employee_profile', blank=True, null=True)    
    def __str__(self):
        return f'{self.name}'

class Attendance(models.Model):
    STATUS_CHOICE = [
        ('Full_Day', 'Full_Day'),
        ('Half_Day', 'Half_Day'),
        ]
    status = models.CharField(choices=STATUS_CHOICE,
                              max_length=255, blank=True, null=True)
    employee_profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    check_in =models.DateTimeField( blank=True, null=True)
    check_out =models.DateTimeField( blank=True, null=True)
    def __str__(self):
        return self.status 
 