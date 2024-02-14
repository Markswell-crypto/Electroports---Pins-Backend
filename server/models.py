from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employee', 'Employee'),
        ('teacher', 'Teacher'),
        ('developer', 'Developer')
    ]

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), nullable=False)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Laptop(db.Model):
    NEW = 'new'
    USED = 'used'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (USED, 'Used'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    brand = db.relationship('Brand', backref=db.backref('laptops', lazy=True))

class Phone(db.Model):
    NEW = 'new'
    USED = 'used'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (USED, 'Used'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    brand = db.relationship('Brand', backref=db.backref('phones', lazy=True))

class Accessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class SoundDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref=db.backref('orders', lazy=True))

class OrderItem(db.Model):
    COMPONENT_CHOICES = [
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('accessory', 'Accessory'),
        ('sound device', 'Sound Device'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    component_type = db.Column(db.String(20), nullable=False)
    component_id = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    order = db.relationship('Order', backref=db.backref('order_items', lazy=True))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    component_type = db.Column(db.String(20), nullable=False)
    component_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(150), nullable=False)

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))

# create a new user
user = User(role='student')
db.session.add(user)
db.session.commit()

# create a new brand
brand = Brand(name='Apple')
db.session.add(brand)
db.session.commit()

# create a new laptop
laptop = Laptop(brand_id=brand.id, name='MacBook Pro', price=1299, status='new')
db.session.add(laptop)
db.session.commit()

# create a new order
order = Order(user_id=user.id, total_price=1299, order_date=datetime.now())
db.session.add(order)
db.session.commit()

# create a new order item
order_item = OrderItem(component_type='laptop', component_id=laptop.id, order_id=order.id)
db.session.add(order_item)
db.session.commit()

# create a new review
review = Review(user_id=user.id, component_type='laptop', component_id=laptop.id, rating=5, comment='Great laptop!')
db.session.add(review)
db.session.commit()



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)