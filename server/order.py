from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import Order, OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/electroports.db'
db = SQLAlchemy(app)
api = Api(app)

class OrderResource(Resource):
    def get(self, order_id):
        order = Order.query.get(order_id)
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
        
class OrderItemResource(Resource):
    def get(self, item_id):
        item = OrderItem.query.get(item_id)
        if item:
            return {
                'id': item.id,
                'component_type': item.component_type,
                'component_id': item.component_id,
                'order_id': item.order_id,
                'quantity': item.quantity
            }
        else:
            return {'message': 'Order Item not found'}, 404
        
api.add_resource(OrderResource, '/order/<int:order_id>')
api.add_resource(OrderItemResource, '/orderitem/<int:item_id>')