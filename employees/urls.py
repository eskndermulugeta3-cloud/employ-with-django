from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),              # home page
    path('employees/', views.employee_list),  # list page
    path('add/', views.add_employee, name='add_employee'),  # add employee page
    path('update/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.employee_list, name='employee_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
