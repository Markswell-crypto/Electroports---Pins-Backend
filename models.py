from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    orders = db.relationship('Order', backref='customer', lazy=True)

class Brand(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo_url = db.Column(db.String(255), nullable=True)

class Phone(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  
    description = db.Column(db.Text, nullable=True)

    brand = db.relationship('Brand', backref='phones')
    reviews = db.relationship('Review', back_populates='phone')

class Laptop(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(255), nullable=True)  
    description = db.Column(db.Text, nullable=True)

    brand = db.relationship('Brand', backref='laptops')
    reviews = db.relationship('Review', back_populates='laptop')

class Accessory(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=True) 
    description = db.Column(db.Text, nullable=True)
    reviews = db.relationship('Review', back_populates='accessory')

class SoundDevice(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=True)  
    description = db.Column(db.Text, nullable=True)
    reviews = db.relationship('Review', back_populates='sound_device')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(150), nullable=False)
    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'))
    phone = db.relationship('Phone', back_populates='reviews')
    laptop_id = db.Column(db.Integer, db.ForeignKey('laptop.id'))
    laptop = db.relationship('Laptop', back_populates='reviews')
    accessory_id = db.Column(db.Integer, db.ForeignKey('accessory.id'))
    accessory = db.relationship('Accessory', back_populates='reviews')
    sound_device_id = db.Column(db.Integer, db.ForeignKey('sound_device.id'))
    sound_device = db.relationship('SoundDevice', back_populates='reviews')



class Order(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

class OrderItem(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    component_type = db.Column(db.String(20), nullable=False)
    component_id = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
