from flask_restful import Resource, reqparse
from models import db, Accessory

accessory_parser = reqparse.RequestParser()
accessory_parser.add_argument('name', type=str, help='Accessory name', required=True)
accessory_parser.add_argument('price', type=int, help='Accessory price', required=True)
accessory_parser.add_argument('image', type=str, help='Image URL', required=False)
accessory_parser.add_argument('description', type=str, help='Accessory description', required=False)  # Add description field

class AccessoriesResource(Resource):
    def get(self):
        try:
            accessories = Accessory.query.all()
            return {
                "accessories": [
                    {
                        "id": accessory.id,
                        "name": accessory.name,
                        "price": accessory.price,
                        "image": accessory.image,
                        "description": accessory.description  # Add description field
                    }
                    for accessory in accessories
                ]
            }
        except Exception as e:
            return {"message": "An error occurred while retrieving accessories.", "error": str(e)}, 500

    def post(self):
        args = accessory_parser.parse_args()
        new_accessory = Accessory(
            name=args['name'],
            price=args['price'],
            image=args.get('image'),
            description=args.get('description')  # Add description field
        )

        try:
            db.session.add(new_accessory)
            db.session.commit()
            return {
                "accessory": {
                    "id": new_accessory.id,
                    "name": new_accessory.name,
                    "price": new_accessory.price,
                    "image": new_accessory.image,
                    "description": new_accessory.description  # Add description field
                }
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the accessory.", "error": str(e)}, 500

class AccessoryByIDResource(Resource):
    def get(self, id):
        accessory = Accessory.query.get(id)

        if not accessory:
            return {"message": "Accessory not found."}, 404

        return {
            "accessory": {
                "id": accessory.id,
                "name": accessory.name,
                "price": accessory.price,
                "image": accessory.image,
                "description": accessory.description  # Add description field
            }
        }

    def delete(self, id):
        accessory = Accessory.query.get(id)

        if not accessory:
            return {"message": "Accessory not found."}, 404

        try:
            db.session.delete(accessory)
            db.session.commit()
            return {"message": "Accessory deleted successfully."}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the accessory.", "error": str(e)}, 500

    def patch(self, id):
        accessory = Accessory.query.get(id)

        if not accessory:
            return {"message": "Accessory not found."}, 404

        args = accessory_parser.parse_args()

        try:
            accessory.name = args['name']
            accessory.price = args['price']
            accessory.image = args.get('image', accessory.image)
            accessory.description = args.get('description', accessory.description)  # Add description field
            db.session.commit()
            return {
                "accessory": {
                    "id": accessory.id,
                    "name": accessory.name,
                    "price": accessory.price,
                    "image": accessory.image,
                    "description": accessory.description  # Add description field
                }
            }
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the accessory.", "error": str(e)}, 500
