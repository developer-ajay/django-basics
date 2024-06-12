from django.urls import path

from employees import views


urlpatterns = [
    path('list/', views.home, name='home'),
    path('<int:pk>/',views.employeeDetails,name='employeeDetails')

]