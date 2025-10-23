from flask import Blueprint
from flask_restful import Api

# Create blueprints
auth_bp = Blueprint('auth', __name__)
products_bp = Blueprint('products', __name__)
categories_bp = Blueprint('categories', __name__)
orders_bp = Blueprint('orders', __name__)
reviews_bp = Blueprint('reviews', __name__)

# Create APIs
auth_api = Api(auth_bp)
products_api = Api(products_bp)
categories_api = Api(categories_bp)
orders_api = Api(orders_bp)
reviews_api = Api(reviews_bp)