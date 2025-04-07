from flask_socketio import emit, join_room, leave_room
from . import socketio

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('message', {'msg': f"{data['username']} has joined the chat."}, room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    emit('message', {'msg': f"{data['username']}: {data['msg']}"}, room=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    emit('message', {'msg': f"{data['username']} has left the chat."}, room=room)
  
