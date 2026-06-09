from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    class_room = models.ForeignKey('ClassRoom', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

class ClassRoom(models.Model):
    class_name = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()

    def str(self):
        return f"{self.class_name} - {self.capacity}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.subject_name

class Teacher(models.Model):
  
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20,unique=True)
    hire_date = models.DateField()
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"

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
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.student} - {self.status}"