from django.shortcuts import render, redirect
from django.http import HttpResponse

# ✅ Auth imports (ONLY ONCE)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Employee
from .forms import EmployeeForm


# 🏠 HOME
@login_required
def home(request):
    return HttpResponse("hi there! Welcome to the Employee Management System.")


# 🔒 DASHBOARD (MAIN PAGE AFTER LOGIN)
@login_required
def dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'employees/dashboard.html', {'employees': employees})


# 🔒 EMPLOYEE LIST
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})


# 🔒 ADD EMPLOYEE
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')   # ✅ FIXED (no hardcoded URL)

    else:
        form = EmployeeForm()

    return render(request, 'employees/add.html', {'form': form})


# 🔒 UPDATE EMPLOYEE
@login_required
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')   # ✅ FIXED

    return render(request, 'employees/update.html', {'form': form})


# 🔒 DELETE EMPLOYEE
@login_required
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')   # ✅ FIXED

    return render(request, 'employees/delete.html', {'employee': employee})


# 🔐 LOGIN SYSTEM
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')   # ✅ go to dashboard
        else:
            return render(request, 'employees/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'employees/login.html')


# 🚪 LOGOUT
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')   # ✅ use name, not URL