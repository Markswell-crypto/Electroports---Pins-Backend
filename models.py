from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employee', 'Employee'),
        ('teacher', 'Teacher'),
        ('developer', 'Developer')
    ]

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), nullable=False)

class Brand(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo_url = db.Column(db.String(255), nullable=True)  

class Laptop(db.Model, SerializerMixin):
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
    image_url = db.Column(db.String(255), nullable=True)  

    brand = db.relationship('Brand', backref=db.backref('laptops', lazy=True))

class Phone(db.Model, SerializerMixin):
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
    image_url = db.Column(db.String(255), nullable=True)  

    brand = db.relationship('Brand', backref=db.backref('phones', lazy=True))

class Accessory(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  

class SoundDevice(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  


class Order(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref=db.backref('orders', lazy=True))

class OrderItem(db.Model, SerializerMixin):
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

class Review(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    component_type = db.Column(db.String(20), nullable=False)
    component_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(150), nullable=False)

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
