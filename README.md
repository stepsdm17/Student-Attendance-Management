
# Student Attendance Management

    A simple Student Attendance Management System built with Django to manage a student attendance system. The project allows CRUD operations for **students**, **classes**, **subjects**, **teachers**, **attendance and **attendance_detail** using relational tables.


## Features

- **Student Management**: Create, list, view, update, and delete students.
- **Class Management**: Create, list, view, update, and delete classes.
- **Subject Management**: Create, list, view, update, and delete subjects.
- **Teacher Management**: Create, list, view, update, and delete teachers.
- **Attendance Management**: Create, list, view, update, and delete attendance.
- **Authentication**: User authentication and logout.


## Tech Stack

- **Python 3.x**
- **Django 4.x**
- **SQLite** 
- **Django Template**
- **Django Model**
- **Django ModelForm**
- **Function-Based View or Class-Based View**
- **URL routing**
- **ForeignKey relationship**
- **PyJWT**
- **Bootstrap or basic CSS**



## Project Structure

```
Student-Attendance-Management/
│
├── manage.py
│
├── Student_management_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── Attendance/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── authentication.py
    ├── templates/
    │   ├── base.html
    │   ├── login.html
    │   ├── logout.html
    │   ├── dashboard.html
    │   ├── students/
    │   │   ├── list.html
    │   │   ├── detail.html
    │   │   ├── create.html
    │   │   ├── edit.html
    │   │   └── delete.html
    │   ├── classes/
    │   │   ├── list.html
    │   │   ├── detail.html
    │   │   ├── create.html
    │   │   └── delete.html
    │   ├── subjects/
    │   │   ├── list.html
    │   │   ├── detail.html
    │   │   ├── create.html
    │   │   └── delete.html
    │   ├── teachers/
    │   │   ├── list.html
    │   │   ├── detail.html
    │   │   ├── create.html
    │   │   └── delete.html
    │   ├── attendance/
    │   │   ├── list.html
    │   │   ├── detail.html
    │   │   ├── create.html
    │   │   └── mark.html
    └── static/
        ├── css/
        │   └── style.css
        └── js/
            └── script.js
```


---

### Authentication Testing

```
{
    "username": "testing",
    "password": "itsdm17"

}
```



## Testing Requirements

Ensure you test all CRUD operations for each resource:

1. Login and get JWT token
2. Access API without token (should return 401)
3. Access API with token (should succeed)
4. Create student
5. Create class
6. Create subject
7. Create teacher
8. Create attendance
9. List all students
10. View student detail
11. Update student
12. Delete student
13. List all classes
14. View class detail
15. Update class
16. Delete class
17. List all subjects
18. View subject detail
19. Update subject
20. Delete subject
21. List all teachers
22. View teacher detail
23. Update teacher
24. Delete teacher
25. Create attendance session
26. View attendance session list
27. View attendance session detail
28. Update attendance session
29. Delete attendance session


## Model relationships

| Model          | Key Relationships                                                                 |
|----------------|-----------------------------------------------------------------------------------|
| **Class**      | → Many `Student`<br>→ Many `Attendance`                                             |
| **Student**    | → One `Class`<br>→ Many `AttendanceDetail`                                          |
| **Subject**    | ↔ Many `Teacher` (Many-to-Many)<br>→ Many `Attendance`                            |
| **Teacher**    | ↔ Many `Subject` (Many-to-Many)<br>→ Many `Attendance`                             |
| **Attendance** | → One `Class`<br>→ One `Subject`<br>→ One `Teacher`<br>→ Many `AttendanceDetail`    |
| **AttendanceDetail** | → One `Attendance`<br>→ One `Student`   

### Class Model

Relationships:
- One-to-Many with Student: Each class can have multiple students.
- One-to-Many with Attendance: Each class can have multiple attendance sessions.

### Student Model

Relationships:
- Many-to-One with Class: Each student belongs to one class (class_room).
- One-to-Many with AttendanceDetail: Each student can have multiple attendance records.

### Subject Model

Relationships:
- Many-to-Many with Teacher: A subject can be taught by multiple teachers, and a teacher can teach multiple subjects.
- One-to-Many with Attendance: Each subject can have multiple attendance sessions.

### Teacher Model

Relationships:
- Many-to-Many with Subject: A teacher can teach multiple subjects (and vice versa).
One-to-Many with Attendance: Each teacher can conduct multiple attendance sessions.

### Attendance Model

Relationships:
- Many-to-One with Class: Each attendance session is linked to one class.
- Many-to-One with Subject: Each session is for one subject.
- Many-to-One with Teacher: Each session is conducted by one teacher.
- One-to-Many with AttendanceDetail: Each session has multiple student attendance records.

### AttendanceDetail Model

Relationships:
- Many-to-One with Attendance: Each detail record belongs to one attendance session.
- Many-to-One with Student: Each record is for one student.

---

## Author of this project

Developed and Designed by SOK Sorya, Prak Sereyvisal and Chhun Menghour.
Lecturer by Mr.Ratana, Web Development with Django.

## License

This project is for educational and personal use only, and was developed as a practical project.

---