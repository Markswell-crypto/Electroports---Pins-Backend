from flask_restful import Resource, reqparse
from models import db, Accessory

accessory_parser = reqparse.RequestParser()
accessory_parser.add_argument('name', type=str, help='Accessory name', required=True)
accessory_parser.add_argument('price', type=int, help='Accessory price', required=True)
accessory_parser.add_argument('image_url', type=str, help='Image URL', required=False)

class AccessoriesResource(Resource):
    def get(self):
        try:
            accessories = Accessory.query.all()
            return {"accessories": [{"id": accessory.id, "name": accessory.name,
                                     "price": accessory.price, "image_url": accessory.image_url}
                                    for accessory in accessories]}
        except Exception as e:
            return {"message": "An error occurred while retrieving accessories.", "error": str(e)}, 500

    def post(self):
        args = accessory_parser.parse_args()
        new_accessory = Accessory(name=args['name'], price=args['price'], image_url=args.get('image_url'))

        try:
            db.session.add(new_accessory)
            db.session.commit()
            return {"accessory": {"id": new_accessory.id, "name": new_accessory.name,
                                  "price": new_accessory.price, "image_url": new_accessory.image_url}}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the accessory.", "error": str(e)}, 500

class AccessoryByIDResource(Resource):
    def get(self, id):
        accessory = Accessory.query.get(id)

        if not accessory:
            return {"message": "Accessory not found."}, 404

        return {"accessory": {"id": accessory.id, "name": accessory.name,
                              "price": accessory.price, "image_url": accessory.image_url}}

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
            accessory.image_url = args.get('image_url', accessory.image_url)
            db.session.commit()
            return {"accessory": {"id": accessory.id, "name": accessory.name,
                                  "price": accessory.price, "image_url": accessory.image_url}}
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the accessory.", "error": str(e)}, 500

