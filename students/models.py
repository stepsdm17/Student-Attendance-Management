from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    class_room = models.ForeignKey('ClassRoom', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

