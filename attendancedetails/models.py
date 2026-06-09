from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Attendance, Student

class AttendanceDetail(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('permission', 'Permission'),
    ]
    
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.student} - {self.status}"
