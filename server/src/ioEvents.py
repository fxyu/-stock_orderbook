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

    @socket.on('clent_get_1m_kdata')
    def client_get_1m_kdata(code):
        if GlobalHandler.quote_ctx == None:
            print('No quote_ctx')
            return []

        code = 'HK.HSImain'
        ret, data = quote_ctx.get_cur_kline(code, 100, ft.SubType.K_1M, ft.AuType.QFQ) 
        if ret == ft.RET_OK:
            print(data)
            print(data['turnover_rate'][0])   # 取第一条的换手率
            print(data['turnover_rate'].values.tolist())   # 转为list

        #        code             time_key   open  close   high    low    volume      turnover  pe_ratio  turnover_rate  last_close
        # 0  HK.00700  2020-03-27 00:00:00  390.0  382.4  390.0  381.8  28738698  1.103966e+10    35.466        0.00301       381.8
        # 1  HK.00700  2020-03-30 00:00:00  371.8  376.6  380.0  371.6  21838731  8.188543e+09    34.928        0.00229       382.4
        # 0.00301
        # [0.00301, 0.00229]
        else:
            print('error:', data)
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



