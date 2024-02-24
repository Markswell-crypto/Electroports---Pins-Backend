from flask_restful import Resource, reqparse
from models import db, Review

review_parser = reqparse.RequestParser()
review_parser.add_argument('user_id', type=int, help='User ID', required=True)
review_parser.add_argument('component_type', type=str, help='Component Type', required=True)
review_parser.add_argument('component_id', type=int, help='Component ID', required=True)
review_parser.add_argument('rating', type=int, help='Rating', required=True)
review_parser.add_argument('comment', type=str, help='Comment', required=True)

class ReviewsResource(Resource):
    def get(self):
        try:
            reviews = Review.query.all()
            if not reviews:
                return {"message": "No reviews found."}, 404
            return {
                "reviews": [
                    {
                        "id": review.id,
                        "comment": review.comment,
                        "phone_id": review.phone_id,
                        "laptop_id": review.laptop_id,
                        "accessory_id": review.accessory_id,
                        "sound_device_id": review.sound_device_id
                    }
                    for review in reviews
                ]
            }
        except Exception as e:
            return {"message": "An error occurred while retrieving reviews.", "error": str(e)}, 500

    def post(self):
        try:
            args = review_parser.parse_args()
            new_review = Review(
                comment=args['comment'],
                phone_id=args.get('phone_id'),
                laptop_id=args.get('laptop_id'),
                accessory_id=args.get('accessory_id'),
                sound_device_id=args.get('sound_device_id')
            )

            db.session.add(new_review)
            db.session.commit()

            return {
                "review": {
                    "comment": new_review.comment,
                    "phone_id": new_review.phone_id,
                    "laptop_id": new_review.laptop_id,
                    "accessory_id": new_review.accessory_id,
                    "sound_device_id": new_review.sound_device_id
                }
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the review.", "error": str(e)}, 500

class ReviewByIDResource(Resource):
    def delete(self, id):
        try:
            review = Review.query.get(id)
            if not review:
                return {"message": "Review not found."}, 404
            db.session.delete(review)
            db.session.commit()
            return {"message": "Review deleted successfully."}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the review.", "error": str(e)}, 500

    def patch(self, id):
        try:
            args = review_parser.parse_args()
            review = Review.query.get(id)
            if not review:
                return {"message": "Review not found."}, 404
            review.comment = args['comment']
            review.phone_id = args.get('phone_id')
            review.laptop_id = args.get('laptop_id')
            review.accessory_id = args.get('accessory_id')
            review.sound_device_id = args.get('sound_device_id')
            db.session.commit()
            return {
                "review": {
                    "comment": review.comment,
                    "phone_id": review.phone_id,
                    "laptop_id": review.laptop_id,
                    "accessory_id": review.accessory_id,
                    "sound_device_id": review.sound_device_id
                }
            }
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the review.", "error": str(e)}, 500
