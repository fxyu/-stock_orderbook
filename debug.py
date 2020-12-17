import numpy as np

data = {
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

print(bid_ask_spread)