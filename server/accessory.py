from flask_restful import Resource, reqparse
from models import db, Accessory

accessory_parser = reqparse.RequestParser()
accessory_parser.add_argument('name', type=str, help='Accessory name', required=True)
accessory_parser.add_argument('price', type=int, help='Accessory price', required=True)

class AccessoriesResource(Resource):
    def get(self):
        accessories = Accessory.query.all()
        return {"accessories": [{"id": accessory.id, "name": accessory.name, "price": accessory.price}
                                for accessory in accessories]}

    def post(self):
        args = accessory_parser.parse_args()
        new_accessory = Accessory(name=args['name'], price=args['price'])

        db.session.add(new_accessory)
        db.session.commit()

        return {"accessory": {"id": new_accessory.id, "name": new_accessory.name,
                              "price": new_accessory.price}}, 201

class AccessoryByIDResource(Resource):
    def delete(self, id):
        accessory = Accessory.query.get(id)

        if not accessory:
            return {"message": "Accessory not found."}, 404

        db.session.delete(accessory)
        db.session.commit()

        return {"message": "Accessory deleted successfully."}, 204

    def patch(self, id):
        accessory = Accessory.query.get(id)

        if not accessory:
            return {"message": "Accessory not found."}, 404

        args = accessory_parser.parse_args()
        accessory.name = args['name']
        accessory.price = args['price']

        db.session.commit()

        return {"access
