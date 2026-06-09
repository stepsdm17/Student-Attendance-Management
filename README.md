@ -1,4 +1,172 @@
# Welcome to your organization's demo respository
This code repository (or "repo") is designed to demonstrate the best GitHub has to offer with the least amount of noise.
# Food Menu API

The repo includes an `index.html` file (so it can render a web page), two GitHub Actions workflows, and a CSS stylesheet dependency.
A simple REST API built with **Django REST Framework** to manage a food menu system. The project allows CRUD operations for **categories**, **menu items**, **customers**, and **orders** using relational tables or ForeignKeys.

---

## Features

- **Category Management**: Create, list, view, update, and delete categories.
- **Menu Item Management**: Create, list, view, update, and delete menu items.
- **Customer Management**: Create, list, view, update, and delete customers.
- **Order Management**: Create, list, view, update, and delete orders.
- **Order Item Management**: Create, list, view, update, and delete order items.
- **Authentication**: User authentication using JSON Web Tokens (JWT).
- **RESTful Endpoints**: Clean, predictable API endpoints following REST conventions.
- **DRF Browsable API**: Explore and test your API directly in the browser.

---

## Tech Stack

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework (DRF)**
- **ModelSerializer**
- **ViewSet or APIView**
- **Router or path URL**
- **SQLite** (default database)
- **Postman** (for API testing)
- **JWT** (JSON Web Tokens)
- **TokenBlacklist** (Token blacklisting)

---

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
4. Create category
5. Create menu item with category
6. Create customer
7. Create order with customer
8. Add order item to order
9. List all orders
10. View order detail
11. Update order status
12. Delete order item
13. Delete order

---

## Author of this project

Developed and Designed by SOK Sorya, Prak Sereyvisal and Chhun Menghour.
Lecturer by Mr.Ratana, Web Development with Django.

## License

This project is for educational and personal use only, and was developed as a practical project.

---