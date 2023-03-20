from django.shortcuts import render, HttpResponse
from .models import Teacher, Employee

# Create your views here.

def abc(request):
    a = Teacher.objects.all()
    a = Teacher.objects.get(mobile = 1434524675)
    a = Teacher.objects.filter(lastname = "Patil")
    a = Teacher.objects.all().count()  
    a = Teacher.objects.all()[:4]
    a = Teacher.objects.all()[1:5]
    a = Teacher.objects.all()[0]  
    a = Teacher.objects.all().order_by('mobile') 
    a = Teacher.objects.filter(firstname__startswith = 'A') 
    a = Teacher.objects.filter(email__startswith = 'k') 
    a = Teacher.objects.filter(email__endswith = 'm') 
    a = Teacher.objects.get(firstname__exact = 'Komal') 
    a = Teacher.objects.get(lastname__contains = 'c')     
    print(a)
    return HttpResponse('ok')

def mnb(request):
    m = Employee.objects.all()
    m = Employee.objects.all().count()
    m = Employee.objects.all().order_by('emp_id') 
    m = Employee.objects.filter(emp_fname__startswith = 'V')
    m = Employee.objects.filter(emp_id__endswith = 'h')
    m = Employee.objects.get(emp_dept = 'IT')
    m = Employee.objects.filter(emp_lname__endswith = 'e')
    m = Employee.objects.filter(emp_fname__endswith = 'l')
    m = Employee.objects.all().order_by('emp_dept')
    m = Employee.objects.get(emp_lname__startswith = 's')

    print(m)
    return HttpResponse("hii")
