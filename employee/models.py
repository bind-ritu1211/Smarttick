from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class State(models.Model):
    names = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):

    SEX_CHOICE = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('BOTH', 'BOTH')
    ]
    
    gender = models.CharField(choices=SEX_CHOICE,
                              max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    manager_name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'{self.name}'



class Attendance(models.Model):

    STATUS_CHOICE = [
        ('Full_Day', 'Full_Day'),
        ('Half_Day', 'Half_Day'),
        ]

    status = models.CharField(choices=STATUS_CHOICE,
                              max_length=255, blank=True, null=True)
    employee_profile = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, blank=True, null=True)
    check_in =models.DateTimeField( blank=True, null=True)
    check_out =models.DateTimeField( blank=True, null=True)

    def __str__(self):
        return self.status
 