from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app.config import config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    
    # Register routes
    api = Api(app)
    
    from app.routes.auth import AuthRegister, AuthLogin, AuthProfile
    from app.routes.products import ProductList, ProductDetail
    from app.routes.categories import CategoryList
    
    # Auth routes
    api.add_resource(AuthRegister, '/api/auth/register')
    api.add_resource(AuthLogin, '/api/auth/login')
    api.add_resource(AuthProfile, '/api/auth/profile')
    
    # Product routes
    api.add_resource(ProductList, '/api/products')
    api.add_resource(ProductDetail, '/api/products/<int:product_id>')
    
    # Category routes
    api.add_resource(CategoryList, '/api/categories')
    
    return app