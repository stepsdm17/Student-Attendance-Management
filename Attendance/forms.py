from django import forms
from .models import Student, Class, Subject, Teacher, Attendance, AttendanceDetail

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'class_room']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'capacity']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'code', 'description']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['employee_id', 'first_name', 'last_name', 'email', 'phone', 'hire_date', 'subjects']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
        widgets['subjects'] = forms.CheckboxSelectMultiple()

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['session_date', 'class_room', 'subject', 'teacher']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
        }

class AttendanceDetailForm(forms.ModelForm):
    class Meta:
        model = AttendanceDetail
        fields = ['student', 'status', 'notes']
        widgets = {
            'status': forms.RadioSelect(choices=AttendanceDetail.STATUS_CHOICES),
        }