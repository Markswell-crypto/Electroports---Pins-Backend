from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User, bcrypt

# User Registration Resource
class UserRegistrationResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            

            if not username or not password or not email:
                return {"error": "Username, password, and email are required."}, 400

            # Check email format
            if not "@" in email or not "." in email:
                return {"error": "Invalid email format."}, 400

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return {"error": "Email is already taken."}, 400

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password, email=email)
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User registered successfully."}, 201
        except Exception as e:
            return {"error": "Failed to register user. Please try again later."}, 500

# User Login Resource
class UserLoginResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return {"error": "Email and password are required."}, 400

            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                access_token = create_access_token(identity=user.email)  # Use email as identity
                return {"access_token": access_token}, 200
            else:
                return {"error": "Invalid email or password."}, 401
        except Exception as e:
            return {"error": "Failed to log in. Please try again later."}, 500


# User Resource (Get user information)
class UserResource(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = User.query.filter_by(username=current_user).first()

            if user:
                return {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                }, 200
            else:
                return {"message": "User not found."}, 404
        except Exception as e:
            return {"error": "Failed to retrieve user information."}, 500
