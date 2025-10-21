# GemCart Backend API

A comprehensive RESTful API for a luxury jewelry e-commerce platform built with Flask-RESTful, featuring JWT authentication, role-based access control, and complete CRUD operations.

## 🚀 Features

- **RESTful API** built with Flask-RESTful
- **JWT Authentication** with role-based access control (RBAC)
- **PostgreSQL Database** with SQLAlchemy ORM
- **Image Upload** with Cloudinary integration and optimization
- **Email Integration** using SendGrid
- **API Documentation** with Swagger/OpenAPI
- **Pagination** for all list endpoints
- **Data Validation** with Marshmallow schemas
- **Error Handling** with comprehensive error responses

## 🏗️ Architecture

```
app/
├── models/          # Database models
├── routes/          # API endpoints
├── schemas/         # Marshmallow schemas for validation
├── services/        # Business logic services
├── utils/           # Utility functions and decorators
└── __init__.py      # App factory
```

## 📋 Requirements

- Python 3.8+
- PostgreSQL
- Cloudinary account (for image uploads)
- SendGrid account (for emails)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd gemcart/backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```env
DATABASE_URL=postgresql://username:password@localhost/gemcart_db
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
CLOUDINARY_CLOUD_NAME=your-cloudinary-cloud-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret
SENDGRID_API_KEY=your-sendgrid-api-key
SENDGRID_FROM_EMAIL=noreply@gemcart.com
```

5. **Database Setup**
```bash
# Create PostgreSQL database
createdb gemcart_db

# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Run the application**
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | User login |
| GET | `/api/auth/profile` | Get user profile |
| PUT | `/api/auth/profile` | Update user profile |

### Product Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/products` | Get products with pagination/filtering | No |
| POST | `/api/products` | Create new product | Seller/Admin |
| GET | `/api/products/{id}` | Get product details | No |
| PUT | `/api/products/{id}` | Update product | Owner/Admin |
| DELETE | `/api/products/{id}` | Delete product | Owner/Admin |

### Order Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/orders` | Get user orders | Customer |
| POST | `/api/orders` | Create new order | Customer |
| GET | `/api/orders/{id}` | Get order details | Owner |

### Category Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories` | Get all categories |

### Review Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/reviews` | Get reviews | No |
| POST | `/api/reviews` | Create review | Customer |

### Admin Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/admin/dashboard` | Get dashboard stats | Admin |
| GET | `/api/admin/users` | Get all users | Admin |

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## 👥 User Roles

- **Customer**: Can browse products, place orders, write reviews
- **Seller**: Can manage their own products + customer permissions
- **Admin**: Full access to all resources

## 📊 Pagination

List endpoints support pagination with the following parameters:

- `page`: Page number (default: 1)
- `per_page`: Items per page (default: varies by endpoint, max: 100)

Response format:
```json
{
  "items": [...],
  "pagination": {
    "page": 1,
    "pages": 5,
    "per_page": 20,
    "total": 100,
    "has_prev": false,
    "has_next": true
  }
}
```

## 🔍 Filtering & Search

### Products
- `search`: Search in title and description
- `category`: Filter by category name
- `min_price`, `max_price`: Price range filtering
- `sort`: Sort by `price_asc`, `price_desc`, `name_asc`, `name_desc`, `newest`

## 📝 Sample Requests

### Register User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "customer"
  }'
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'
```

### Get Products
```bash
curl "http://localhost:5000/api/products?page=1&per_page=12&category=Rings&sort=price_asc"
```

### Create Product (Seller/Admin)
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "title": "Diamond Engagement Ring",
    "description": "Beautiful 1-carat diamond ring",
    "price": 2500.00,
    "inventory_count": 10,
    "sku": "RING-001",
    "category_ids": [1]
  }'
```

## 🚀 Deployment

### Using Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set environment variables in Render dashboard
4. Deploy!

### Environment Variables for Production

```env
DATABASE_URL=postgresql://...
SECRET_KEY=production-secret-key
JWT_SECRET_KEY=production-jwt-secret
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
SENDGRID_API_KEY=...
SENDGRID_FROM_EMAIL=...
FLASK_ENV=production
```

## 🧪 Testing

```bash
# Run tests (if implemented)
pytest

# Test API endpoints
curl -X GET http://localhost:5000/api/products
```

## 📖 Swagger Documentation

Visit `http://localhost:5000/apidocs/` for interactive API documentation.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support, email support@gemcart.com or create an issue in the repository.