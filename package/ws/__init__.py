from package import app
from flask_socketio import SocketIO, ConnectionRefusedError
from package.models.user import User
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.event
def connect(sid, environ, auth):
    if not auth or 'token' not in auth:
        raise ConnectionRefusedError('Authentication token is required')
    user = User.query.filter_by(usertoken=auth['token']).first()
    if not user:
        raise ConnectionRefusedError('Invalid authentication token')
    
    socketio.emit('response', {'data': 'Connected successfully'})
    print('Client connected:', auth) 