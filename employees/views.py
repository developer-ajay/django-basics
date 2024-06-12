from django.shortcuts import render

from employees.models import Employee

# Create your views here.

def home(request):
    employees  = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request , 'home.html' ,context)