# Django API Project Setup Guide

This document explains the full setup for the APIFirstProject Django API, including dependencies, database setup, run steps, and routes.

## 1) Project Structure

- APIFirstProject/manage.py
- APIFirstProject/APIFirstProject/settings.py
- APIFirstProject/APIFirstProject/urls.py
- APIFirstProject/templates/index.html
- APIFirstProject/AppAPI/models.py
- APIFirstProject/AppAPI/views.py
- APIFirstProject/AppAPI/serializers.py
- APIFirstProject/AppAPI/urls.py

## 2) Python Environment Setup

From workspace root (example: C:/File/Code/Python/DjangoAPI):

    python -m venv .venv

Activate on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Upgrade pip (optional but recommended):

    python -m pip install --upgrade pip

## 3) Install Required Packages

    pip install Django djangorestframework django-ckeditor Pillow django-cors-headers

## 4) Create Project and App (if starting from scratch)

    django-admin startproject APIFirstProject
    cd APIFirstProject
    python manage.py startapp AppAPI

## 5) Configure Settings

Update APIFirstProject/settings.py:

- Add apps to INSTALLED_APPS:
    - corsheaders
  - AppAPI
  - rest_framework
  - ckeditor
  - ckeditor_uploader

- Add middleware at the top of MIDDLEWARE:

        'corsheaders.middleware.CorsMiddleware',

- Add CORS allowed frontend origins (development example):

        CORS_ALLOWED_ORIGINS = [
                'http://127.0.0.1:5500',
                'http://localhost:5500',
                'http://127.0.0.1:3000',
                'http://localhost:3000',
                'http://127.0.0.1:5173',
                'http://localhost:5173',
        ]

- Add Django templates directory:

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

- Add static/media configuration:

    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [BASE_DIR / 'static']

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

- Add CKEditor config:

    CKEDITOR_UPLOAD_PATH = 'uploads/'
    CKEDITOR_CONFIGS = {
        'default': {
            'toolbar': 'full',
            'skin': 'moono',
            'extraPlugins': ','.join([
                'codesnippet',
                'widget',
                'dialog',
            ]),
        },
    }

## 6) Models

In AppAPI/models.py create:

- Category
  - categoryName
  - categoryImage

- Product
  - productName
  - categoryID (ForeignKey to Category)
  - price
  - productDescript (RichTextUploadingField)
  - weight
  - availability
  - shipping
  - productImage
  - productDate

## 7) Admin Registration

In AppAPI/admin.py register:

- Category
- Product

## 8) Serializer

In AppAPI/serializers.py create ProductSerializer for fields:

- id
- productName
- price
- productImage
- productDate

## 9) API Views

In AppAPI/views.py create:

- home (function view) to render templates/index.html
- ProductsListCreate (ListCreateAPIView)
- ProductsUpdateDelete (RetrieveUpdateDestroyAPIView)

## 10) URL Routing

### App-level routes (AppAPI/urls.py)

- /  -> home (render index.html)
- APICategory/  -> CategoriesListCreate
- APICategory/<int:pk>/  -> CategoriesUpdateDelete
- APIProduct/  -> ProductsListCreate
- APIProduct/<int:pk>/  -> ProductsUpdateDelete

### Project-level routes (APIFirstProject/urls.py)

- admin/  -> Django admin
- (root) include AppAPI urls
- api/ include AppAPI urls
- ckeditor/ include ckeditor_uploader urls
- static media serving added in debug mode through django.conf.urls.static.static

## 11) Run Migrations

From APIFirstProject folder (where manage.py is):

    python manage.py makemigrations
    python manage.py migrate

## 12) Create Admin User

    python manage.py createsuperuser

## 13) Run Development Server

    python manage.py runserver

Server URL:

- http://127.0.0.1:8000/

Stop server:

- Ctrl + C

## 14) API Endpoints

Main API endpoint:

- GET/POST http://127.0.0.1:8000/api/APIProduct/

Category API endpoint:

- GET/POST http://127.0.0.1:8000/api/APICategory/

Single item endpoint:

- GET/PUT/PATCH/DELETE http://127.0.0.1:8000/api/APIProduct/<id>/
- GET/PUT/PATCH/DELETE http://127.0.0.1:8000/api/APICategory/<id>/

Because AppAPI urls are also included at root, these also work:

- http://127.0.0.1:8000/APICategory/
- http://127.0.0.1:8000/APICategory/<id>/
- http://127.0.0.1:8000/APIProduct/
- http://127.0.0.1:8000/APIProduct/<id>/

## 15) Quick Test Examples

List products:

    Invoke-WebRequest -Uri http://127.0.0.1:8000/api/APIProduct/ -UseBasicParsing

Create product (example with minimal fields):

    $body = @{ productName = 'Sample Product'; price = '10.00' } | ConvertTo-Json
    Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/APIProduct/ -ContentType 'application/json' -Body $body

## 16) Notes

- The django-ckeditor package currently warns that bundled CKEditor 4 is outdated.
- For production, use a secure editor strategy and production static/media hosting.
- This setup is for development and learning.
