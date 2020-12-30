import eventlet
eventlet.monkey_patch()

import futu as ft
import numpy as np

from .globalHandler import GlobalHandler

class TickerTest(ft.TickerHandlerBase):
    def on_recv_rsp(self, rsp_str):
        ret_code, data = super(TickerTest,self).on_recv_rsp(rsp_str)
        if ret_code != ft.RET_OK:
            print("TickerTest: error, msg: %s" % data)
            return ft.RET_ERROR, data
        # print("TickerTest ", data) # TickerTest自己的处理逻辑
        json = self.gen_text(data)
        GlobalHandler.emit_on_socket('server_newTickData', json)
        return ft.RET_OK, data

    def gen_text(self, data):
        i = data.iloc[0]
        tick_info_str = f"{i.time.split()[-1]} {i.price} {i.volume}"
        return [tick_info_str, int(i.volume)]

class OrderBookTest(ft.OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_str):
        ret_code, data = super(OrderBookTest, self).on_recv_rsp(rsp_str)

        # If some error occur
        if ret_code != ft.RET_OK:
            print("OrderBookTest: error, msg: %s" % data)
            return ft.RET_ERROR, data

        # print("OrderBookTest ", data) # OrderBookTest自己的处理逻辑
        spread = self.gen_json_array(data)
        json = {
            'time' : data['svr_recv_time_bid'],
            'code' : data['code'],
            'data' : spread
        }
        GlobalHandler.emit_on_socket('server_newOrderBookData', json)
        # self.socketIO.emit('server_newOrderBookData', json, broadcast=True)
        return ft.RET_OK, data

    def gen_json_array(self, data):
        x_low = data['Bid'][-1][0]
        x_high= data['Ask'][-1][0]
        step  = abs(data['Bid'][1][0] - data['Bid'][0][0])

        items = {}
        bid_ask_spread = []

        for price in np.arange(x_low,x_high+step,step):
            # print(str(price))
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


class BrokerTest(ft.BrokerHandlerBase):
    def on_recv_rsp(self, rsp_str):
        ret_code, err_or_stock_code, data = super(BrokerTest, self).on_recv_rsp(rsp_str)
        if ret_code != ft.RET_OK:
            print("BrokerTest: error, msg: {}".format(err_or_stock_code))
            return ft.RET_ERROR, data
        print("BrokerTest: stock: {} data: {} ".format(err_or_stock_code, data))  # BrokerTest自己的处理逻辑
        return ft.RET_OK, data


class StockQuoteTest(ft.StockQuoteHandlerBase):
    def on_recv_rsp(self, rsp_str):
        ret_code, data = super(StockQuoteTest,self).on_recv_rsp(rsp_str)
        if ret_code != ft.RET_OK:
            print("StockQuoteTest: error, msg: %s" % data)

            return RET_ERROR, data
        print("StockQuoteTest ", data) # StockQuoteTest自己的处理逻辑
        return ft.RET_OK, data


# class StockQQQ(ft.HandlerBase)

class CurKlineTest(ft.CurKlineHandlerBase):
    def on_recv_rsp(self, rsp_str):
        ret_code, data = super(CurKlineTest,self).on_recv_rsp(rsp_str)
        if ret_code != ft.RET_OK:
            print("CurKlineTest: error, msg: %s" % data)
            return RET_ERROR, data
        GlobalHandler.emit_on_socket('server_newkline', data.to_json(orient="records"))
        # print("CurKlineTest ", data) # CurKlineTest自己的处理逻辑
        return ft.RET_OK, data


"""
a = {
    'code': 'HK.HSImain', 
    'svr_recv_time_bid': '2020-12-15 01:25:00.990', 
    'svr_recv_time_ask': '2020-12-15 01:25:00.990', 
    'Bid': [(26406.0, 3, 3, {}), 
            (26405.0, 4, 4, {}), 
            (26404.0, 2, 2, {}), 
            (26403.0, 3, 3, {}), 
            (26402.0, 5, 5, {}), 
            (26401.0, 4, 4, {}), 
            (26400.0, 3, 3, {}), 
            (26399.0, 7, 7, {}), 
            (26398.0, 3, 3, {}), 
            (26397.0, 4, 4, {})], 
    'Ask': [(26409.0, 4, 4, {}), 
            (26410.0, 3, 3, {}), 
            (26411.0, 4, 4, {}), 
            (26412.0, 2, 2, {}), 
            (26413.0, 5, 5, {}), 
            (26414.0, 4, 4, {}), 
            (26415.0, 4, 4, {}), 
            (26416.0, 3, 3, {}), 
            (26417.0, 4, 4, {}), 
            (26418.0, 3, 3, {})]
    }

    code        time                price   volume  turnover    ticker_direction    sequence             type           push_data_type
0   HK.HSImain  2020-12-15 01:24:49 26410.0 1       26410.0     BUY                 6906164342312402946  AUTO_MATCH     REALTIME
"""

# x_low = data['Bid'][0][0]
# x_high= data['Ask'][-1][0]
# step  = data['Bid'][1][0] - x_low

# items = {}

# for price in range(x_low,x_high+step,step):
#     item[price] = {
#         'price' : price,
#         'contract' : 0
#     }

# for bid in data['Bid']:
#     item[bid[0]]['']


# 'Bid': [[26406.0, 3], 
#         [26405.0, 4], 
#         [26404.0, 2], 
#         [26403.0, 3], 
#         [26402.0, 5], 
#         [26401.0, 4], 
#         [26400.0, 3], 
#         [26399.0, 7], 
#         [26398.0, 3], 
#         [26397.0, 4]
        
#         [26409.0, 0], 
#         [26410.0, 0], 
#         [26411.0, 0], 
#         [26412.0, 0], 
#         [26413.0, 0], 
#         [26414.0, 0], 
#         [26415.0, 0], 
#         [26416.0, 0], 
#         [26417.0, 0], 
#         [26418.0, 0]], 


# 'Ask': [[26406.0, 0], 
#         [26405.0, 0], 
#         [26404.0, 0], 
#         [26403.0, 0], 
#         [26402.0, 0], 
#         [26401.0, 0], 
#         [26400.0, 0], 
#         [26399.0, 0], 
#         [26398.0, 0], 
#         [26397.0, 0],
    
#         [26409.0, 4], 
#         [26410.0, 3], 
#         [26411.0, 4], 
#         [26412.0, 2], 
#         [26413.0, 5], 
#         [26414.0, 4], 
#         [26415.0, 4], 
#         [26416.0, 3], 
#         [26417.0, 4], 
#         [26418.0, 3]]