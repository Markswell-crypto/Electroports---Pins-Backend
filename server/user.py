from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models import db, User, bcrypt

class UserRegistrationResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            role = data.get('role')

            if not username or not password or not role:
                return {"error": "Username, password, and role are required."}, 400

            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                return {"error": "Username is already taken."}, 400

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password, role=role)
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User registered successfully."}, 201
        except Exception as e:
            return {"error": str(e)}, 500

class UserLoginResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                access_token = create_access_token(identity=username)
                return {"access_token": access_token}, 200
            else:
                return {"error": "Invalid username or password."}, 401
        except Exception as e:
            return {"error": str(e)}, 500

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
            return {"error": str(e)}, 500