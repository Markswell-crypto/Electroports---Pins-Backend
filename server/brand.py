from flask_restful import Resource, reqparse
from models import db, Brand

brand_parser = reqparse.RequestParser()
brand_parser.add_argument('name', type=str, help='Brand name', required=True)

class BrandsResource(Resource):
    def get(self):
        brands = Brand.query.all()
        return {"brands": [{"id": brand.id, "name": brand.name} for brand in brands]}

    def post(self):
        args = brand_parser.parse_args()
        new_brand = Brand(name=args['name'])

        db.session.add(new_brand)
        db.session.commit()

        return {"brand": {"id": new_brand.id, "name": new_brand.name}}, 201

class BrandByIDResource(Resource):
    def delete(self, id):
        brand = Brand.query.get(id)

        if not brand:
            return {"message": "Brand not found."}, 404

        db.session.delete(brand)
        db.session.commit()

        return {"message": "Brand deleted successfully."}, 204

    def patch(self, id):
        brand = Brand.query.get(id)

        if not brand:
            return {"message": "Brand not found."}, 404

        args = brand_parser.parse_args()
        brand.name = args['name']

        db.session.commit()

        return {"brand": {"id": brand.id, "name": brand.name}}


