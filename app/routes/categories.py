from flask_restful import Resource
from app.models import Category

class CategoryList(Resource):
    def get(self):
        categories = Category.query.filter_by(is_active=True).all()
        return {
            'categories': [{
                'id': c.id,
                'name': c.name,
                'slug': c.slug,
                'description': c.description,
                'product_count': c.product_count
            } for c in categories]
        }, 200