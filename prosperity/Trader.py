# The Python code below is the minimum code that is required in a submission file:
# 1. The "datamodel" imports at the top. Using the typing library is optional.
# 2. A class called "Trader", this class name should not be changed.
# 3. A run function that takes a tradingstate as input and outputs a "result" dict.

from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order, Trade

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        result = {}
        for product in state.order_depths.keys():
                order_depth : OrderDepth = state.order_depths[product]
                orders : List[Order] = []
                # market_trades : Trade = state.market_trades[product]
                # order_dict = dict()
                # order_dict = {
                #     'BAGUETTE':1,
                #     'BANANAS':2,
                #     'BERRIES':3,
                #     'COCONUTS':4,
                #     'DIP':5,
                #     'DIVING_GEAR':6,
                #     'PEARLS':7,
                #     'PICNIC_BASKET':8,
                #     'PINA_COLADAS':9,
                #     'UKULELE':10,
                # }
                # a fair value for pearls, calculate this afterwords
                # acceptable_price = 1
                acceptable_price = calculate_acceptable_price(product)
                order_limit = calculate_order_limit(product)
                profit = 0
                total_sell = 0
                total_buy = 0
                # k = list()
                # i = order_dict.get_value(product)

                # for j in range(1,10):
                #     k[j] = list(dict())



                if len(order_depth.sell_orders) >0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]


                    if best_ask < acceptable_price[0] :
                        # print("BUY", str(-best_ask_volume)+ "x", best_ask)
                        # dict = {
                        #      best_ask:best_ask_volume
                        #      }
                        # k[i].append(dict)
                        orders.append(Order(product, best_ask,-best_ask_volume))
                        total_buy += best_ask_volume*best_ask
                        #print(orders)

                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > (acceptable_price[0]+ acceptable_price[1])/2:
                        # print("SELL", str(best_bid_volume) + "x", best_bid)                        
                        orders.append(Order(product, best_bid, -best_bid_volume))
                        total_sell+= best_bid_volume*best_bid
                result[product] = orders
                profit += total_sell - total_buy
                
        # print(f"profit is {profit}")

        return result
    


def calculate_acceptable_price(product):
    if product == 'PEARLS': 
        return [9999.764343,10000.71712]
    elif product == 'BANANAS':
        return [4808.374679,4853.024026]
    elif product == 'COCONUTS':
        return [7919.869686,7984.942623]
    elif product == 'PINA_COLADAS':
        return [14869.5898,14980.09281]
    elif product == 'BERRIES':
        return [3890.842107,3926.403546]
    elif product == 'DIVING_GEAR':
        return [99216.09501,99745.53553]
    elif product =='PICNIC_BASKET':
        return [73954.66535,74098.13963]
    elif product =='UKULELE':
        return [20718.56719,21020.86239]
    elif product =='BAGUETTE':
        return [12106.66216,12326.19219]
    elif product == 'DIP':
        return [7080.569267,7092.061485]
        

def calculate_order_limit(product):
    if product == 'PEARLS': 
        return 20
    elif product == 'BANANAS':
        return 20
    elif product == 'COCONUTS':
        return 600
    elif product == 'PINA_COLADAS':
        return 300
    elif product == 'BERRIES':
        return 250
    elif product == 'DIVING_GEAR':
        return 50
    elif product =='PICNIC_BASKET':
        return 70
    elif product =='UKULELE':
        return 70
    elif product =='BAGUETTE':
        return 150
    elif product == 'DIP':
        return 300