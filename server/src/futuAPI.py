import futu as ft
from .futuHandlers import TickerTest, OrderBookTest, BrokerTest
from .globalHandler import GlobalHandler


def connect_to_ftOPEND():
    # ft.set_futu_debug_model(True)
    ft.SysConfig.set_all_thread_daemon(True)
    quote_ctx = ft.OpenQuoteContext(host="127.0.0.1", port=11111)
    GlobalHandler.quote_ctx = quote_ctx
    
    quote_ctx.start()
    quote_ctx.set_handler(TickerTest())
    quote_ctx.set_handler(OrderBookTest())
    # quote_ctx.set_handler(BrokerTest())
    
    code = 'HK.HSImain'
    ret, err_message = quote_ctx.subscribe(code, [
                                ft.SubType.QUOTE, 
                                ft.SubType.ORDER_BOOK, 
                                ft.SubType.TICKER,
                                # ft.SubType.BROKER
                                ],
                                is_detailed_orderbook=True)

    if ret == ft.RET_OK:
        print('subscribe success!')
    else:
        print(err_message)

    return quote_ctx