from flask_socketio import SocketIO

socketio = SocketIO()

def init_sockets(app):
    socketio.init_app(app)

    @socketio.on("message")
    def handle_message(msg):
        print("Mensaje recibido:", msg)
        socketio.emit("response", {"data": msg})
