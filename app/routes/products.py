from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Product, User

class ProductList(Resource):
    def get(self):
        products = Product.query.filter_by(is_active=True).all()
        return {
            'products': [{
                'id': p.id,
                'title': p.title,
                'description': p.description,
                'price': float(p.price),
                'image_url': p.image_url,
                'average_rating': p.average_rating
            } for p in products]
        }, 200
    
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user.is_seller():
            return {'message': 'Only sellers can create products'}, 403
        
        data = request.get_json()
        product = Product(
            title=data['title'],
            description=data.get('description'),
            price=data['price'],
            sku=data['sku'],
            inventory_count=data.get('inventory_count', 0),
            seller_id=user_id
        )
        
        db.session.add(product)
        db.session.commit()
        
        return {'message': 'Product created successfully', 'product_id': product.id}, 201

class ProductDetail(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return {
            'product': {
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'price': float(product.price),
                'sku': product.sku,
                'inventory_count': product.inventory_count,
                'image_url': product.image_url,
                'average_rating': product.average_rating,
                'review_count': product.review_count
            }
        }, 200