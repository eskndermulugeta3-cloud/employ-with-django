from django.db import models

# Create your models here.

# Import Django database tool

class Employee(models.Model):
# Create a table called Employee

    name = models.CharField(max_length=100)
    # Text field (employee name)

    email = models.EmailField()
    # Email field (validates email)

    position = models.CharField(max_length=50)
    # Job role (Manager, Developer, etc.)

    def __str__(self):
    # How object appears in admin panel
        return self.name





