from django.urls import path

from employees import views


urlpatterns = [
    path('list/', views.home),

]