from flask import request, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Order
from .notifications import send_notification

@login_required
def place_order():
    data = request.get_json()
    new_order = Order(user_id=current_user.id, product=data['product'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    send_notification(current_user.id, "Your order has been placed.")
    return jsonify({"message": "Order placed successfully"}), 201

@login_required
def track_order(order_id):
    order = Order.query.get(order_id)
    if order and order.user_id == current_user.id:
        return jsonify({"order_id": order.id, "status": order.status})
    return jsonify({"message": "Order not found"}), 404
  
