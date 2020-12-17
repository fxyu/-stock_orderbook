import futu as ft
from pynput import keyboard

# from src.handlers import TickerTest, OrderBookTest, BrokerTest

quote_ctx = ft.OpenQuoteContext(host="127.0.0.1", port=11111)

quote_ctx.start()                               # 开启异步数据接收
# quote_ctx.set_handler(TickerTest())   # 设置用于异步处理数据的回调对象(可派生支持自定义)
# quote_ctx.set_handler(OrderBookTest())
# quote_ctx.set_handler(BrokerTest())
 
market = ft.Market.HK
code = 'HK.08493'
ret, err_message = quote_ctx.subscribe(code, [
                                ft.SubType.QUOTE, 
                                ft.SubType.ORDER_BOOK, 
                                ft.SubType.TICKER,
                                ft.SubType.BROKER,
                                ft.SubType.K_1M
                            ],
                            is_detailed_orderbook=True)

if ret == ft.RET_OK:
    print('subscribe success!')

    ret, data = quote_ctx.get_rt_ticker(code, 2)  # 获取港股00700最近2个逐笔
    if ret == ft.RET_OK:
        print(data)
        print(data['turnover'][0])   # 取第一条的成交金额
        # print(data['turnover'].values.tolist())   # 转为list
        # ['code', 'time', 'price', 'volume', 'turnover', 'ticker_direction', 'sequence', 'type']

        i = data.iloc[0]
        tick_info_str = f"{i.time.split()[-1]} {i.price} {i.volume}"

    ret, bid_frame_table, ask_frame_table = quote_ctx.get_broker_queue(code)   # 获取一次经纪队列数据
    if ret == ft.RET_OK:
        print(bid_frame_table)
    else:
        print('error:', bid_frame_table)

    # code                     HK.08493
    # bid_broker_id                8466
    # bid_broker_name    富途证券国际(香港)有限公司
    # bid_broker_pos                  1
    # order_id                      N/A
    # order_volume                  N/A
    # Name: 0, dtype: object

    ret, data = quote_ctx.get_cur_kline('HK.08493', 10, ft.SubType.K_1M, ft.AuType.QFQ)  # 获取港股00700最近2个K线数据
    if ret == ft.RET_OK:
        print(data)
        print(data['turnover_rate'][0])   # 取第一条的换手率
        print(data['turnover_rate'].values.tolist())   # 转为list
    else:
        print('error:', data)

else:
    print(err_message)


def on_release(key):
    if key == keyboard.Key.esc:
        quote_ctx.close()
        return False

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()


""" subtype
# ft.SubType

ft.SubType.NONE  未知
ft.SubType.QUOTE  基礎報價
ft.SubType.ORDER_BOOK  擺盤
ft.SubType.TICKER  逐筆
ft.SubType.BROKER  經紀隊列

ft.SubType.RT  分時
ft.SubType.K_DAY  日 K
ft.SubType.K_5M  5 分 K
ft.SubType.K_15M  15 分 K
ft.SubType.K_30M  30 分 K
ft.SubType.K_60M  60 分 K
ft.SubType.K_1M  1 分 K
ft.SubType.K_WEEK  週 K
ft.SubType.K_MON  月 K
ft.SubType.K_QURATER  季 K
ft.SubType.K_YEAR  年 K
ft.SubType.K_3M  3 分 K
"""


