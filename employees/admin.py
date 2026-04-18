from django.contrib import admin
# Import admin system

from .models import Employee
# Import Employee model

admin.site.register(Employee)
# Register model in admin panel