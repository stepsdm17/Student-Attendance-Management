from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import jwt
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
from .models import Student, Class, Subject, Teacher, Attendance, AttendanceDetail
from .forms import StudentForm, ClassForm, SubjectForm, TeacherForm, AttendanceForm, AttendanceDetailForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token = jwt.encode({
                'user_id': user.id,
                'username': user.username,
                'exp': datetime.utcnow() + timedelta(hours=1),
                'iat': datetime.utcnow()
            }, settings.JWT_SETTINGS['SECRET_KEY'], algorithm='HS256')
            
            request.session['jwt_token'] = token
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_classes = Class.objects.count()
    total_subjects = Subject.objects.count()
    total_teachers = Teacher.objects.count()
    total_attendance = Attendance.objects.count()
    
    today_attendance = Attendance.objects.filter(session_date=timezone.now().date()).count()
    
    context = {
        'total_students': total_students,
        'total_classes': total_classes,
        'total_subjects': total_subjects,
        'total_teachers': total_teachers,
        'total_attendance': total_attendance,
        'today_attendance': today_attendance,
    }
    return render(request, 'dashboard.html', context)

# Student Views
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/create.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully')
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully')
        return redirect('student_list')
    return render(request, 'students/delete.html', {'student': student})

# Class Views
@login_required
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'classes/list.html', {'classes': classes})

@login_required
def class_detail(request, pk):
    class_room = get_object_or_404(Class, pk=pk)
    return render(request, 'classes/detail.html', {'class_room': class_room})

@login_required
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class created successfully')
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'classes/create.html', {'form': form})

@login_required
def class_delete(request, pk):
    class_room = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_room.delete()
        messages.success(request, 'Class deleted successfully')
        return redirect('class_list')
    return render(request, 'classes/delete.html', {'class_room': class_room})

# Subject Views
@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})

@login_required
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subjects/detail.html', {'subject': subject})

@login_required
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject created successfully')
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subjects/create.html', {'form': form})

@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, 'Subject deleted successfully')
        return redirect('subject_list')
    return render(request, 'subjects/delete.html', {'subject': subject})

# Teacher Views
@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/list.html', {'teachers': teachers})

@login_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'teacher': teacher})

@login_required
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher created successfully')
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/create.html', {'form': form})

@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully')
        return redirect('teacher_list')
    return render(request, 'teachers/delete.html', {'teacher': teacher})

# Attendance Views
@login_required
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance/list.html', {'attendances': attendances})

@login_required
def attendance_detail(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    details = AttendanceDetail.objects.filter(attendance=attendance)
    return render(request, 'attendance/detail.html', {'attendance': attendance, 'details': details})

@login_required
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save()
            # Create attendance details for all students in the class
            students = Student.objects.filter(class_room=attendance.class_room)
            for student in students:
                AttendanceDetail.objects.create(
                    attendance=attendance,
                    student=student,
                    status='absent'  # Default status
                )
            messages.success(request, 'Attendance session created successfully')
            return redirect('attendance_detail', pk=attendance.id)
    else:
        form = AttendanceForm()
    return render(request, 'attendance/create.html', {'form': form})

@login_required
def mark_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        for detail in attendance.attendancedetail_set.all():
            status = request.POST.get(f'status_{detail.id}')
            notes = request.POST.get(f'notes_{detail.id}')
            detail.status = status
            detail.notes = notes
            detail.save()
        
        attendance.status = 'completed'
        attendance.save()
        messages.success(request, 'Attendance marked successfully')
        return redirect('attendance_detail', pk=pk)
    
    details = attendance.attendancedetail_set.all()
    return render(request, 'attendance/mark.html', {'attendance': attendance, 'details': details})