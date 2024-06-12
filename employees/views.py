from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from employees.models import Employee

# Create your views here.

def home(request):
    employees  = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request , 'home.html' ,context)

def employeeDetails(request , pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee' : employee
    }
    return render(request , 'employeeDetails.html',context)