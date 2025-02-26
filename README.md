Django E-commerce API

Overview

This project is a RESTful API for an e-commerce platform built using Django and Django Rest Framework (DRF). It includes custom user authentication, category and product management, soft deletion, bulk upload functionality using Celery, and JWT authentication.

Features

1. Authentication & User Management

Custom User Model (Email-based authentication)

JWT Authentication (using djangorestframework-simplejwt)

Endpoints:

POST /auth/register/ → Register a user

POST /auth/login/ → Login

POST /auth/logout/ → Logout (Blacklist token)

PATCH /auth/update/ → Update user details

POST /auth/forgot-password/ → Send password reset link via email

2. Category & Subcategory Management

Supports dynamic subcategories using a Parent-Child Relationship

CRUD operations allowed for Admin only

Endpoints:

POST /category/ → Create category (Admin Only)

GET /category/ → List all categories (Public)

GET /category/{id}/ → Retrieve a specific category

PATCH /category/{id}/ → Update category (Admin Only)

DELETE /category/{id}/ → Soft delete category (Admin Only)

3. Product Management

Each product belongs to a category

CRUD operations for Admin, Read for all users

Endpoints:

POST /product/ → Create a product (Admin Only)

GET /product/ → List all products (Public)

GET /product/{id}/ → Retrieve a specific product

PATCH /product/{id}/ → Update product details (Admin Only)

DELETE /product/{id}/ → Soft delete product (Admin Only)

4. Bulk Upload (Using Celery)

Users can upload a JSON file containing category and product data

Celery processes the file asynchronously to avoid request timeouts

Endpoint:

POST /upload/ → Upload JSON file (Admin Only)

5. Soft Delete Instead of Permanent Deletion

Uses an is_deleted=True flag instead of deleting records

API filters out soft-deleted records automatically

Technology Stack

Backend: Django, Django Rest Framework (DRF)

Database: PostgreSQL

Task Queue: Celery

Broker: Redis/RabbitMQ (for Celery task processing)

Authentication: JWT (using djangorestframework-simplejwt)

Background Processing: Celery (for bulk uploads)

Version Control: Git

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

PostgreSQL

Redis (for Celery tasks)

Step 1: Clone the Repository

git clone https://github.com/your-repo/ecommerce-api.git
cd ecommerce-api

Step 2: Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Step 3: Configure Environment Variables

Create a .env file and add your database, Redis, and secret key configuration:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/ecommerce_db
CELERY_BROKER_URL=redis://localhost:6379/0

Step 4: Apply Migrations

python manage.py makemigrations
python manage.py migrate

Step 5: Create a Superuser

python manage.py createsuperuser

Step 6: Run the Server

python manage.py runserver

Step 7: Start Celery Worker

celery -A ecommerce_api worker --loglevel=info

Testing

Run tests using:

python manage.py test

API Documentation

You can test API endpoints using Postman or via Django's browsable API.

Contributing

Feel free to submit issues or pull requests to improve the project!

License

This project is open-source and available under the MIT License.

