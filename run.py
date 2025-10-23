import os
from app import create_app, db
from app.models import User, Product, Category, Order, Review

def deploy():
    """Run deployment tasks."""
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    
    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Create sample data if none exists
        if not User.query.first():
            create_sample_data()

def create_sample_data():
    """Create sample data for development"""
    try:
        # Create admin user
        admin = User(
            username='admin',
            email='admin@gemcart.com',
            first_name='Admin',
            last_name='User',
            role='admin'
        )
        admin.set_password('admin123')
        
        # Create categories
        categories_data = [
            {'name': 'Rings', 'slug': 'rings', 'description': 'Engagement and wedding rings'},
            {'name': 'Necklaces', 'slug': 'necklaces', 'description': 'Pendants and chains'},
            {'name': 'Earrings', 'slug': 'earrings', 'description': 'Studs and hoops'}
        ]
        
        db.session.add(admin)
        
        for cat_data in categories_data:
            category = Category(**cat_data)
            db.session.add(category)
        
        db.session.commit()
        print("Sample data created successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error creating sample data: {e}")

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    
    with app.app_context():
        db.create_all()
        if not User.query.first():
            create_sample_data()
    
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)