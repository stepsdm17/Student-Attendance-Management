from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Teacher(models.Model):
  
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    hire_date = models.DateField()
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"

