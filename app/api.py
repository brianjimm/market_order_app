from flask import Blueprint
from flask_restful import Api, Resource
from .orders import place_order, track_order

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

class OrderResource(Resource):
    def post(self):
        return place_order()
    
class OrderStatusResource(Resource):
    def get(self, order_id):
        return track_order(order_id)

api.add_resource(OrderResource, "/order")
api.add_resource(OrderStatusResource, "/order/<int:order_id>")
