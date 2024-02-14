from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///electro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_REFRESH_COOKIE_PATH'] = '/refresh'
app.config['JWT_REFRESH_COOKIE_SECURE'] = False
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = False

db.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)
api = Api(app)
CORS(app)


if __name__ == '__main__':
    app.run(port=5500, debug=True)
