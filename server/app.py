# import eventlet
# eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

from src.ioEvents import socketIOEvents
from src.futuAPI import connect_to_ftOPEND

from src.globalHandler import GlobalHandler

import signal
import sys



from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'ThisIsAVerySecretStringThatIWillNotBeAbleToDecrypt!'
socketio = SocketIO(app, async_mode='threading', cors_allowed_origins='*')
socketIOEvents(socketio)
GlobalHandler.socketio = socketio

quote_ctx = None

# simple routing
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    data = {}
    GlobalHandler.emit_on_socket('server_test', data)
    return "Sent"

@app.route('/stop', methods=['GET'])
def stopServer():
    global quote_ctx
    if quote_ctx is not None:
        quote_ctx.stop()
        quote_ctx.close()
    return "Sent"

@app.route('/start', methods=['GET'])
def startFutuAPI():
    global quote_ctx
    if quote_ctx == None:
        quote_ctx = connect_to_ftOPEND()
    return "Started"

## Kill futu api and kill the app
def signal_handler(sig, frame):
    global quote_ctx
    if quote_ctx is not None:
        quote_ctx.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    print("Start Server!")
    socketio.run(app, host="0.0.0.0", \
        debug=True,
        # cors_allowed_origins="*",
        port=5005)
    print('End')
    
    
# @app.route('/search/<word>', methods=['GET'])
# def search(word):
#     print('Search from get method (word : {})'.format(word))
#     socketio.emit('server_newWord', (word, db.get(word)), broadcast=True)
#     return 'submitted'


# @app.route('/playAudio', methods=['GET'])
# def playAudio():
#     socketio.emit('server_playAudio', (), broadcast=True)
#     return 'played'

# @app.route('/new')
# def new():
#     data = {
#         'array':list(range(16)),
#         'title':"Testing"
#     }
#     socketio.emit('cNewMatrix', data)
#     return "Sent"