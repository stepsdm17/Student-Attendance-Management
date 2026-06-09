from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

