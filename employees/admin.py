from django.contrib import admin
from employees.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
     list_display = ('first_name', 'last_name', 'designation', 'email_address','phone_number')
     search_fields = ('first_name', 'last_name', 'email_address')

admin.site.register(Employee, EmployeeAdmin)