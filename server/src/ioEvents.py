from flask import Flask, request
from flask_socketio import SocketIO, send, emit

from .globalHandler import GlobalHandler
import futu as ft

import json

def socketIOEvents(socketio):
#====== DEFAULT EVENT ==============
    @socketio.on('message')
    def handle_message(msg):
        print(msg)

    @socketio.on('json')
    def handle_json(json):
        print(json)

    @socketio.on('connect')
    def handle_new_connection():
        print('A user connected')

    @socketio.on('disconnect')
    def handle_new_connection():
        print('A user disconnected')

#======= Stock Spread EVENT =========
    @socketio.on('client_history')
    def client_history(code):
        if GlobalHandler.quote_ctx == None:
            print('No quote_ctx')
            return []

        code = 'HK.HSImain'
        ret_code, data = GlobalHandler.quote_ctx.get_rt_ticker(code, 1000)
        if ret_code == ft.RET_OK:
            x = [[f"{i.time.split()[-1]} {i.price} {i.volume}",int(i.volume)] for idx, i in data.iterrows()]
            return x
        else:
            print(data)

        return []

#======= webDict EVENT ==============
    # @socketio.on('client_searchWord')
    # def searchWord(word):
    #     print('Search word : {}'.format(word))
    #     x = db.get(word)
    #     socketio.emit('server_newWord', (word, x), broadcast=True)

    # @socketio.on('client_getHistory')
    # def getHistory(x):
    #     print('client getHistory')
    #     x = db.getHistory()
    #     return x



