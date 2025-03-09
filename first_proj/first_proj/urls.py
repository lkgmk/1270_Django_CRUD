"""
URL configuration for first_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, add_opt
from first_app.views import emp_details, create_emp_details, \
    emp_details_home, delete_emp_details, update_emp_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('addition/', add_opt),
    path('emp_details/', emp_details, name="emp_details_url"),
    path('emp_details_home/', emp_details_home, name="emp_details_home"),
    path('emp_details_form/', create_emp_details, name="emp_details_form"),
    path('delete_emp_details/<pk>', delete_emp_details, name="delete_empdetail_url"),
    path('update_emp_details/<pk>', update_emp_details, name="update_empdetail_url"),
    path('update_emp_details_data/', update_emp_details, name="update_empdetail_data_url"),
]
