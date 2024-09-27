# **Inventory Management System - Backend API**

### **Objective**
This project implements a backend API for an Inventory Management System using Django Rest Framework (DRF). It supports CRUD operations for inventory items, uses JWT-based authentication for security, and integrates caching with Redis for performance optimization. The project also includes logging and unit tests for monitoring and verifying API functionality.

### **Features**
- **JWT Authentication**: Secure API endpoints with JWT.
- **CRUD Operations**: Create, Read, Update, and Delete inventory items.
- **Caching with Redis**: Improve performance by caching frequently accessed items.
- **PostgreSQL Database**: Store inventory items using PostgreSQL.
- **Error Handling**: Implement appropriate error codes for each endpoint.

---

## **Installation Guide**

### **Prerequisites**
1.**Python 3.9.6+**
2.**PostgreSQL**
3.**Redis**
4.**virtualenv** for managing dependencies

### **Step-by-Step Installation**

1. **Clone the Repository**
   ```bash
   git clone 
   cd my_project
Set Up a Virtual Environment Using venv:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configure the Database

Set up PostgreSQL and create a new database.
Update the DATABASES setting in settings.py to connect to your PostgreSQL instance.
Run Migrations
python manage.py migrate

Set Up Redis Ensure Redis is running on your machine or configure the Redis server settings in settings.py.

Run the Development Server

python manage.py runserver


All API endpoints require JWT authentication.

Register: /api/account/sign-up/
Register a new user with POST request.

Login: /api/account/login/
Login and retrieve a JWT token with POST request.

**CRUD Endpoints**

Create Item-
Method: POST
Path: /api/item/item/create-item/
Request Body:
{
  "name": "Item Name",
  "description": "Item Description"
}
Response: JSON object with created item details.
Error Codes:400: Item already exists.


Read Item-
Method: GET
Path: /api/item/create-item/
Response: JSON object with item details.
Error Codes:404: Item not found.


Update Item-
Method: PUT
Path: /api/items/update-item/<id>/
Request Body:
{
  "name": "Updated Name",
  "description": "Updated Description"
}
Response: JSON object with updated item details.
Error Codes:404: Item not found.


Delete Item-
Method: DELETE
Path: /api/item/delete-item/<id>/
Response: Success message.
Error Codes:404: Item not found.


Redis Caching
The Read Item endpoint caches frequently accessed items in Redis. Once an item is accessed, it is stored in Redis, speeding up subsequent retrievals.
