from django.contrib import admin
from .models import Student, ClassRoom, Subject, Teacher, Attendance, AttendanceDetail

admin.site.register(Student)
admin.site.register(ClassRoom)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(AttendanceDetail)