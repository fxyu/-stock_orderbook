from flask import Flask, request
from flask_socketio import SocketIO, send, emit

from .globalHandler import GlobalHandler
import futu as ft

import json
import numpy as np

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

    @socketio.on('client_get_1m_kdata')
    def client_get_1m_kdata(code):
        if GlobalHandler.quote_ctx == None:
            print('No quote_ctx')
            return []

        code = 'HK.HSImain'
        ret, data = GlobalHandler.quote_ctx.get_cur_kline(code, 1000, ft.SubType.K_1M, ft.AuType.QFQ) 
        if ret == ft.RET_OK:
            print(f"get current k line of {code}")
            # print(data)
            # SERVER_HISTORY1MDATA
            emit('server_history1mdata', data.to_json(orient="records"))
            return True

        #        code             time_key   open  close   high    low    volume      turnover  pe_ratio  turnover_rate  last_close
        # 0  HK.00700  2020-03-27 00:00:00  390.0  382.4  390.0  381.8  28738698  1.103966e+10    35.466        0.00301       381.8
        # 1  HK.00700  2020-03-30 00:00:00  371.8  376.6  380.0  371.6  21838731  8.188543e+09    34.928        0.00229       382.4
        # 0.00301
        # [0.00301, 0.00229]
        else:
            print('error:', data)

        return []

    @socketio.on('client_get_ob_history')
    def client_get_ob_history(code):
        print("client_get_ob_history received")
        if GlobalHandler.quote_ctx == None:
            print('No quote_ctx')
            return []

        def gen_json_array(data):
            x_low = data['Bid'][-1][0]
            x_high= data['Ask'][-1][0]
            step  = round(abs(data['Bid'][1][0] - data['Bid'][0][0]),2)

            items = {}
            bid_ask_spread = []

            for price in np.arange(x_low,x_high+step,step):
                # print(str(price))
                price = round(price,2)
                items[str(price)] = {
                    'price' : price,
                    'ask' : 0,
                    'bid' : 0
                }

            for bid in data['Bid']:
                items[str(bid[0])]['bid'] = bid[1]

            for ask in data['Ask']:
                items[str(ask[0])]['ask'] = ask[1]

            for key, val in items.items():
                bid_ask_spread += [val]

            return bid_ask_spread

        # code = 'HK.HSImain'
        code = 'HK.00883'
        ret, data = GlobalHandler.quote_ctx.get_order_book(code, num=10)
        if ret == ft.RET_OK:
            print(data)
            spread = gen_json_array(data)
            json = {
                'time' : data['svr_recv_time_bid'],
                'code' : data['code'],
                'data' : spread
            }
            GlobalHandler.emit_on_socket('server_newOrderBookData', json)
            return True
        else:
            print('error:', data)

        return []

    @socketio.on('client_get_stock_quote')
    def client_get_1m_kdata(code):
        if GlobalHandler.quote_ctx == None:
            print('No quote_ctx')
            return {"code": "err", "msg": "server no quote_ctx"}

        code = 'HK.HSImain'
        ret, data = GlobalHandler.quote_ctx.get_stock_quote(code) 

        if ret != ft.RET_OK:
            print('error:', data)
            return {"code": "err", "msg": data}

        print(data)
        print(f"[SUCCESS] Get stock quote of {code}")
        emit('server_stock_quote', data.to_json(orient="records"))
        return {"code": "ok", "msg": "success"}

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



