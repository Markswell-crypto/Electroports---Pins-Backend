from flask_restful import Resource, reqparse
from models import db, Order, OrderItem

order_parser = reqparse.RequestParser()
order_parser.add_argument('user_id', type=int, help='User ID', required=True)
order_parser.add_argument('total_price', type=int, help='Total price', required=True)
order_parser.add_argument('order_date', type=str, help='Order date', required=True)

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return {"orders": [{"id": order.id, "user_id": order.user_id, "total_price": order.total_price,
                            "order_date": order.order_date.isoformat()} for order in orders]}

    def post(self):
        args = order_parser.parse_args()
        new_order = Order(user_id=args['user_id'], total_price=args['total_price'], order_date=args['order_date'])

        db.session.add(new_order)
        db.session.commit()

        return {"order": {"id": new_order.id, "user_id": new_order.user_id, "total_price": new_order.total_price,
                          "order_date": new_order.order_date.isoformat()}}, 201

class OrderByIDResource(Resource):
    def get(self, id):
        order = Order.query.get(id)
        if order:
            return {
                'id': order.id,
                'user_id': order.user_id,
                'total_price': order.total_price,
                'order_date': order.order_date.isoformat(),
                'order_items': [{'component_type': item.component_type, 'component_id': item.component_id, 'quantity': item.quantity} for item in order.order_items]
            }
        else:
            return {'message': 'Order not found'}, 404

    def delete(self, id):
        order = Order.query.get(id)

        if not order:
            return {"message": "Order not found."}, 404

        db.session.delete(order)
        db.session.commit()

        return {"message": "Order deleted successfully."}, 204

    def patch(self, id):
        order = Order.query.get(id)

        if not order:
            return {"message": "Order not found."}, 404

        args = order_parser.parse_args()
        order.user_id = args['user_id']
        order.total_price = args['total_price']
        order.order_date = args['order_date']

        db.session.commit()

        return {"order": {"id": order.id, "user_id": order.user_id, "total_price": order.total_price,
                          "order_date": order.order_date.isoformat()}}