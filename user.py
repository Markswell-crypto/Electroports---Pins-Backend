from flask import jsonify, request, current_app, send_from_directory
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from models import db, User, bcrypt
import logging
import os

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
                refresh_token = create_refresh_token(identity=user.email)
                return {"access_token": access_token, "refresh_token": refresh_token}, 200
            else:
                return {"error": "Invalid email or password."}, 401
        except Exception as e:
            # Log the exception for debugging
            logging.exception("An error occurred during login:")
            return {"error": "Failed to log in. Please try again later."}, 500

# Refresh Token Resource
class RefreshTokenResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        try:
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user)
            return {"access_token": access_token}, 200
        except Exception as e:
            return {"error": "Failed to refresh access token."}, 500

# User Resource (Get user information)
class UserResource(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = User.query.filter_by(email=current_user).first()

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

    @jwt_required()
    def put(self):
        try:
            current_user = get_jwt_identity()
            user = User.query.filter_by(email=current_user).first()

            if not user:
                return {"message": "User not found."}, 404

            # Check if the request contains a file
            if 'image' not in request.files:
                return {"error": "No file provided."}, 400

            # Get the file from the request
            image = request.files['image']

            # Save the image
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                user.image_url = filename
                db.session.commit()
                return {"message": "Image uploaded successfully.", "image_url": filename}, 200
            else:
                return {"error": "Invalid image file."}, 400
        except UploadNotAllowed:
            return {"error": "File upload not allowed."}, 400
        except Exception as e:
            return {"error": "Failed to upload image."}, 500

    @jwt_required()
    def delete(self):
        try:
            current_user = get_jwt_identity()
            user = User.query.filter_by(email=current_user).first()

            if not user:
                return {"message": "User not found."}, 404

            # Delete the user's image file
            if user.image_url:
                os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], user.image_url))
                user.image_url = None
                db.session.commit()
                return {"message": "Image deleted successfully."}, 200
            else:
                return {"message": "No image to delete."}, 404
        except Exception as e:
            return {"error": "Failed to delete image."}, 500

# Profile Page Resource
class ProfileResource(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = User.query.filter_by(email=current_user).first()

            if user:
                return {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "image_url": user.image_url
                }, 200
            else:
                return {"message": "User not found."}, 404
        except Exception as e:
            return {"error": "Failed to retrieve user profile."}, 500

    @jwt_required()
    def put(self):
        try:
            data = request.get_json()
            current_user = get_jwt_identity()
            user = User.query.filter_by(email=current_user).first()

            if not user:
                return {"message": "User not found."}, 404

            # Update user details
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)

            # Check if a new image file is provided
            if 'image' in request.files:
                image = request.files['image']
                if image and allowed_file(image.filename):
                    filename = secure_filename(image.filename)
                    image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                    # Delete old image if exists
                    if user.image_url:
                        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], user.image_url))
                    user.image_url = filename

            db.session.commit()
            return {"message": "User profile updated successfully."}, 200
        except Exception as e:
            return {"error": "Failed to update user profile."}, 500

# Serve User Images
class ServeImage(Resource):
    def get(self, filename):
        try:
            return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
        except FileNotFoundError:
            return {"error": "Image not found."}, 404

# Helper function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
