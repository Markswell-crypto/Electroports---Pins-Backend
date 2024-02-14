from flask_restful import Resource, reqparse
from models import db, Laptop

laptop_parser = reqparse.RequestParser()
laptop_parser.add_argument('brand_id', type=int, help='Brand ID', required=True)
laptop_parser.add_argument('name', type=str, help='Laptop name', required=True)
laptop_parser.add_argument('price', type=int, help='Laptop price', required=True)
laptop_parser.add_argument('status', type=str, help='Laptop status', required=True)

class LaptopsResource(Resource):
    def get(self):
        laptops = Laptop.query.all()
        return {"laptops": [{"id": laptop.id, "brand_id": laptop.brand_id, "name": laptop.name,
                             "price": laptop.price, "status": laptop.status} for laptop in laptops]}

    def post(self):
        args = laptop_parser.parse_args()
        new_laptop = Laptop(brand_id=args['brand_id'], name=args['name'], price=args['price'], status=args['status'])

        db.session.add(new_laptop)
        db.session.commit()

        return {"laptop": {"id": new_laptop.id, "brand_id": new_laptop.brand_id, "name": new_laptop.name,
                           "price": new_laptop.price, "status": new_laptop.status}}, 201

class LaptopByIDResource(Resource):
    def delete(self, id):
        laptop = Laptop.query.get(id)

        if not laptop:
            return {"message": "Laptop not found."}, 404

        db.session.delete(laptop)
        db.session.commit()

        return {"message": "Laptop deleted successfully."}, 204

    def patch(self, id):
        laptop = Laptop.query.get(id)

        if not laptop:
            return {"message": "Laptop not found."}, 404

        args = laptop_parser.parse_args()
        laptop.brand_id = args['brand_id']
        laptop.name = args['name']
        laptop.price = args['price']
        laptop.status = args['status']

        db.session.commit()

        return {"laptop": {"id": laptop.id, "brand_id": laptop.brand_id, "name": laptop.name,
                           "price": laptop.price, "status": laptop.status}}
