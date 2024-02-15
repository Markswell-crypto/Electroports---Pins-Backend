from flask_restful import Resource, reqparse
from models import db, Phone

phone_parser = reqparse.RequestParser()
phone_parser.add_argument('brand_id', type=int, help='Brand ID', required=True)
phone_parser.add_argument('name', type=str, help='Phone name', required=True)
phone_parser.add_argument('price', type=int, help='Phone price', required=True)
phone_parser.add_argument('status', type=str, help='Phone status', required=True)

class PhonesResource(Resource):
    def get(self):
        try:
            phones = Phone.query.all()
            return {"phones": [{"id": phone.id, "brand_id": phone.brand_id, "name": phone.name,
                                "price": phone.price, "status": phone.status} for phone in phones]}
        except Exception as e:
            return {"message": "An error occurred while retrieving phones.", "error": str(e)}, 500

    def post(self):
        try:
            args = phone_parser.parse_args()
            new_phone = Phone(brand_id=args['brand_id'], name=args['name'], price=args['price'], status=args['status'])

            db.session.add(new_phone)
            db.session.commit()

            return {"phone": {"id": new_phone.id, "brand_id": new_phone.brand_id, "name": new_phone.name,
                              "price": new_phone.price, "status": new_phone.status}}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the phone.", "error": str(e)}, 500

class PhoneByIDResource(Resource):
    def delete(self, id):
        try:
            phone = Phone.query.get(id)

            if not phone:
                return {"message": "Phone not found."}, 404

            db.session.delete(phone)
            db.session.commit()

            return {"message": "Phone deleted successfully."}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the phone.", "error": str(e)}, 500

    def patch(self, id):
        try:
            phone = Phone.query.get(id)

            if not phone:
                return {"message": "Phone not found."}, 404

            args = phone_parser.parse_args()
            phone.brand_id = args['brand_id']
            phone.name = args['name']
            phone.price = args['price']
            phone.status = args['status']

            db.session.commit()

            return {"phone": {"id": phone.id, "brand_id": phone.brand_id, "name": phone.name,
                              "price": phone.price, "status": phone.status}}
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the phone.", "error": str(e)}, 500
