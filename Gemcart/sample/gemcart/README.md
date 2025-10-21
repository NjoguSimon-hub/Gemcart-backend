# 💎 GemCart - Luxury Jewelry & Watches Marketplace

A premium full-stack e-commerce application featuring exquisite jewelry, luxury watches, chains, and precious gems.

## ✨ Enhanced Features

- 💍 **Premium Product Collection**: Rings, necklaces, watches, chains, and gems
- 🔍 **Advanced Search & Filters**: Search by name, category, price range
- 🛍️ **Smart Shopping Cart**: Real-time updates with quantity management
- 📱 **Responsive Design**: Beautiful on all devices
- 👑 **Luxury Indicators**: Special badges for premium items
- 📦 **Stock Management**: Real-time inventory tracking
- 🎆 **Free Shipping**: Worldwide delivery included
- 🔒 **Secure Authentication**: JWT-based user system

## Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd client
npm install
npm start
```

## Test Account
- **Email:** seller@gemcart.com
- **Password:** password
- **Role:** Seller (can create products)

## 💎 Sample Luxury Collection
The application comes with pre-loaded premium products:
- 💙 Ocean's Embrace Sapphire Necklace ($1,250)
- 💍 Vintage Diamond Engagement Ring ($2,800) 
- 🌟 Luxury Swiss Chronograph Watch ($3,500)
- 🔗 Cuban Link Gold Chain ($1,800)
- 💎 Natural Colombian Emerald ($4,200)
- ✨ Rose Gold Tennis Bracelet ($2,200)

## Technology Stack
- **Backend:** Flask, SQLAlchemy, JWT Authentication
- **Frontend:** React, React Router, Context API
- **Styling:** Tailwind CSS
- **Images:** Unsplash API for high-quality jewelry photos

## API Endpoints
- `GET /api/products` - List all products with images
- `GET /api/products/:id` - Get product details
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

Visit http://localhost:3000 to see the jewelry marketplace with beautiful product images!