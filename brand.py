from flask_restful import Resource, reqparse
from models import db, Brand

brand_parser = reqparse.RequestParser()
brand_parser.add_argument('name', type=str, help='Brand name', required=True)
brand_parser.add_argument('logo_url', type=str, help='Logo URL', required=False)

class BrandsResource(Resource):
    def get(self):
        try:
            brands = Brand.query.all()
            return {"brands": [{"id": brand.id, "name": brand.name, "logo_url": brand.logo_url} for brand in brands]}
        except Exception as e:
            return {"message": "An error occurred while fetching brands.", "error": str(e)}, 500

    def post(self):
        try:
            args = brand_parser.parse_args()
            new_brand = Brand(name=args['name'], logo_url=args['logo_url'])

            db.session.add(new_brand)
            db.session.commit()

            return {"brand": {"id": new_brand.id, "name": new_brand.name, "logo_url": new_brand.logo_url}}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the brand.", "error": str(e)}, 500

class BrandByIDResource(Resource):
    def get(self, id):
        try:
            brand = Brand.query.get(id)
            if not brand:
                return {"message": "Brand not found."}, 404

            return {"brand": {"id": brand.id, "name": brand.name, "logo_url": brand.logo_url}}
        except Exception as e:
            return {"message": "An error occurred while fetching the brand.", "error": str(e)}, 500
        
    def patch(self, id):
        try:
            brand = Brand.query.get(id)
            if not brand:
                return {"message": "Brand not found."}, 404

            args = brand_parser.parse_args()
            brand.name = args['name']
            brand.logo_url = args['logo_url']

            db.session.commit()

            return {"brand": {"id": brand.id, "name": brand.name, "logo_url": brand.logo_url}}
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the brand.", "error": str(e)}, 500
        
    def delete(self, id):
        try:
            brand = Brand.query.get(id)
            if not brand:
                return {"message": "Brand not found."}, 404

            db.session.delete(brand)
            db.session.commit()

            return {"message": "Brand deleted successfully."}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the brand.", "error": str(e)}, 500
