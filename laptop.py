from flask_restful import Resource, reqparse
from models import db, Laptop

laptop_parser = reqparse.RequestParser()
laptop_parser.add_argument('brand_id', type=int, help='Brand ID', required=True)
laptop_parser.add_argument('name', type=str, help='Laptop name', required=True)
laptop_parser.add_argument('price', type=int, help='Laptop price', required=True)
laptop_parser.add_argument('status', type=str, help='Laptop status', required=True)
laptop_parser.add_argument('image', type=str, help='Image URL', required=False)
laptop_parser.add_argument('description', type=str, help='Laptop description', required=False)  # Add description field

class LaptopsResource(Resource):
    def get(self):
        try:
            laptops = Laptop.query.all()
            return {
                "laptops": [
                    {
                        "id": laptop.id,
                        "brand_id": laptop.brand_id,
                        "name": laptop.name,
                        "price": laptop.price,
                        "status": laptop.status,
                        "image": laptop.image,
                        "description": laptop.description  # Add description field
                    }
                    for laptop in laptops
                ]
            }
        except Exception as e:
            return {"message": "An error occurred while fetching laptops.", "error": str(e)}, 500

    def post(self):
        args = laptop_parser.parse_args()
        new_laptop = Laptop(
            brand_id=args['brand_id'],
            name=args['name'],
            price=args['price'],
            status=args['status'],
            image=args.get('image'),
            description=args.get('description')  # Add description field
        )

        try:
            db.session.add(new_laptop)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "Error occurred while adding the laptop.", "error": str(e)}, 500

        return {
            "laptop": {
                "id": new_laptop.id,
                "brand_id": new_laptop.brand_id,
                "name": new_laptop.name,
                "price": new_laptop.price,
                "status": new_laptop.status,
                "image": new_laptop.image,
                "description": new_laptop.description  # Add description field
            }
        }, 201

class LaptopByIDResource(Resource):
    def get(self, id):
        try:
            laptop = Laptop.query.get(id)
            if not laptop:
                return {"message": "Laptop not found."}, 404
            return {
                "laptop": {
                    "id": laptop.id,
                    "brand_id": laptop.brand_id,
                    "name": laptop.name,
                    "price": laptop.price,
                    "status": laptop.status,
                    "image": laptop.image,
                    "description": laptop.description  # Add description field
                }
            }
        except Exception as e:
            return {"message": "An error occurred while fetching the laptop.", "error": str(e)}, 500

    def delete(self, id):
        laptop = Laptop.query.get(id)

        if not laptop:
            return {"message": "Laptop not found."}, 404

        try:
            db.session.delete(laptop)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "Error occurred while deleting the laptop.", "error": str(e)}, 500

        return {"message": "Laptop deleted successfully."}, 204

    def patch(self, id):
        laptop = Laptop.query.get(id)

        if not laptop:
            return {"message": "Laptop not found."}, 404

        args = laptop_parser.parse_args()

        try:
            laptop.brand_id = args['brand_id']
            laptop.name = args['name']
            laptop.price = args['price']
            laptop.status = args['status']
            laptop.image = args.get('image', laptop.image)
            laptop.description = args.get('description', laptop.description)  # Add description field
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "Error occurred while updating the laptop.", "error": str(e)}, 500

        return {
            "laptop": {
                "id": laptop.id,
                "brand_id": laptop.brand_id,
                "name": laptop.name,
                "price": laptop.price,
                "status": laptop.status,
                "image": laptop.image,
                "description": laptop.description  # Add description field
            }
        }
