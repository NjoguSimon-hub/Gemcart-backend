# Gemcart Backend

A Flask-based REST API for a jewelry e-commerce platform.

## Features

- User authentication (JWT)
- Product management
- Category management
- Order processing
- Review system

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Run the application:
```bash
python run.py
```

## API Endpoints

### Authentication
- POST `/api/auth/register` - Register user
- POST `/api/auth/login` - Login user
- GET `/api/auth/profile` - Get user profile

### Products
- GET `/api/products` - List products
- POST `/api/products` - Create product (sellers only)
- GET `/api/products/<id>` - Get product details

### Categories
- GET `/api/categories` - List categories

## Database

SQLite database will be created automatically on first run.