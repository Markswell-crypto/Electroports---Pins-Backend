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
        reviews = Review.query.all()
        return {"reviews": [{"id": review.id, "user_id": review.user_id, 
                             "component_type": review.component_type, 
                             "component_id": review.component_id, 
                             "rating": review.rating, 
                             "comment": review.comment} for review in reviews]}

    def post(self):
        args = review_parser.parse_args()
        new_review = Review(user_id=args['user_id'], 
                            component_type=args['component_type'], 
                            component_id=args['component_id'], 
                            rating=args['rating'], 
                            comment=args['comment'])

        db.session.add(new_review)
        db.session.commit()

        return {"review": {"id": new_review.id, "user_id": new_review.user_id, 
                           "component_type": new_review.component_type, 
                           "component_id": new_review.component_id, 
                           "rating": new_review.rating, 
                           "comment": new_review.comment}}, 201

class ReviewByIDResource(Resource):
    def delete(self, id):
        review = Review.query.get(id)

        if not review:
            return {"message": "Review not found."}, 404

        db.session.delete(review)
        db.session.commit()

        return {"message": "Review deleted successfully."}, 204

    def patch(self, id):
        review = Review.query.get(id)

        if not review:
            return {"message": "Review not found."}, 404

        args = review_parser.parse_args()
        review.user_id = args['user_id']
        review.component_type = args['component_type']
        review.component_id = args['component_id']
        review.rating = args['rating']
        review.comment = args['comment']

        db.session.commit()

        return {"review": {"id": review.id, "user_id": review.user_id, 
                           "component_type": review.component_type, 
                           "component_id": review.component_id, 
                           "rating": review.rating, 
                           "comment": review.comment}}
