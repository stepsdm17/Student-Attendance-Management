from django.contrib import admin
from .models import Student, Class, Subject, Teacher, Attendance, AttendanceDetail

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(AttendanceDetail)