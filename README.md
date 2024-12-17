# School Management System Project (Django)

## Overview
The **School Management System** is a web-based application developed using **Django** and **Django Rest Framework (DRF)**. The system is designed to streamline the administrative, library, and student management processes within an educational institution. It supports **role-based access control (RBAC)** to ensure secure and specific functionalities for different user roles: **Admin**, **Office Staff**, and **Librarian**.

## Key Features

### **Admin Role**
- Full access to all system functionalities.
- Manage user accounts for **Office Staff** and **Librarians** (Create, Edit, Delete).
- Perform **CRUD operations** on:
   - **Student Records**  
   - **Library History**  
   - **Fees Records**

### **Office Staff Role**
- Access all student details.
- Manage **Fees History** (Add, Edit, Delete).
- View library borrowing records and student reviews.

### **Librarian Role**
- View-only access to student details.
- Manage and view **Library Borrowing Records**.

## Dashboards

- **Admin Dashboard**: Comprehensive control over the system, user roles, and records.  
- **Office Staff Dashboard**: Access to manage fees and view student/library records.  
- **Librarian Dashboard**: View-only access to library and student records.

## Modules and Functionalities

### **Student Management**
- Perform **CRUD operations** on student details:
   - Name  
   - Division  
   - Roll Number (Enforces unique roll numbers within a division).

### **Library Management**
- Track library borrowing history.  
- Manage borrowing records:
   - Add, Edit, and Delete (Admin only).  
- View borrowing status: Borrowed/Returned.

### **Fees Management**
- Record and manage student fee payments:
   - Amount  
   - Payment Date  
   - Transaction ID  
   - Remarks

## Technologies Used

### **Core Django Libraries**
- **Django**: `5.1.1`
- **Django Rest Framework (DRF)**: `3.15.2`
- **djangorestframework-simplejwt**: `5.3.1`
- **PyJWT**: `2.9.0`
- **jwcrypto**: `1.5.6`
- **sqlparse**: `0.5.1`

### **Other Technologies**
- **Python**: Core programming language.
- **SQLite**: Default database for storing data.
- **JWT Authentication**: Secure user authentication via JSON Web Tokens.
- **venv**: Virtual Environment for project dependency isolation.

## Installation and Setup

Follow these steps to set up and run the project locally:

### **1. Prerequisites**
Ensure you have the following installed:
- **Python >= 3.8**
- **pip** (Python package manager)

### **2. Clone the Repository**
```bash
git clone https://github.com/ASWATHI-P-V/School_Management_System
cd School_Management


###**Future Enhancements**

Implement advanced reporting for admin dashboards.
Add automated email notifications for due payments and book returns.
Integrate a payment gateway for fee payments.
Enhance the user interface with modern front-end libraries.


###**Contributors**

Aswathi PV – Developer
