class GlobalHandler():
    socketio = None
    quote_ctx = None

    @staticmethod
    def emit_on_socket(key,data):
        if GlobalHandler is not None:
            socket = GlobalHandler.socketio
            socket.emit(key, data, broadcast=True)