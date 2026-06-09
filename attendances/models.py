from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .models import ClassRoom, Subject, Teacher

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    
    session_date = models.DateField()
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.session_date} - {self.class_room} - {self.subject}"

