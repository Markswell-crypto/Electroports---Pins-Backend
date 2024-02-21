import os
from datetime import timedelta
from flask import Flask, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db, bcrypt
from user import UserRegistrationResource, UserLoginResource, UserResource
from brand import BrandsResource, BrandByIDResource
from laptop import LaptopsResource, LaptopByIDResource
from phone import PhonesResource, PhoneByIDResource
from accessory import AccessoriesResource, AccessoryByIDResource
from order import OrderResource, OrderByIDResource
from review import ReviewsResource, ReviewByIDResource
from soundDevice import SoundDevicesResource, SoundDeviceByIDResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '3fsfr5gf6g7hhg7'
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_REFRESH_COOKIE_PATH'] = '/refresh'
app.config['JWT_REFRESH_COOKIE_SECURE'] = False
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

api = Api(app)
jwt = JWTManager(app)
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

CORS(app)

with app.app_context():
    db.create_all()
    
@app.route('/')
def welcome():
    return jsonify(message="Welcome to ElectroPorts and Pins API")

api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')
api.add_resource(UserResource, '/user')
api.add_resource(BrandsResource, '/brands')
api.add_resource(BrandByIDResource, '/brands/<int:id>')
api.add_resource(LaptopsResource, '/laptops')
api.add_resource(LaptopByIDResource, '/laptops/<int:id>')
api.add_resource(PhonesResource, '/phones')
api.add_resource(PhoneByIDResource, '/phones/<int:id>')
api.add_resource(AccessoriesResource, '/accessories')
api.add_resource(AccessoryByIDResource, '/accessories/<int:id>')
api.add_resource(OrderResource, '/orders')
api.add_resource(OrderByIDResource, '/orders/<int:id>')
api.add_resource(ReviewsResource, '/reviews')
api.add_resource(ReviewByIDResource, '/reviews/<int:id>')
api.add_resource(SoundDevicesResource, '/sounddevices')
api.add_resource(SoundDeviceByIDResource, '/sounddevices/<int:id>')

if __name__ == '__main__':
    app.run(port=5500, debug=True, use_reloader=True)