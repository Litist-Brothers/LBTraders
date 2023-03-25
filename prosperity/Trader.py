# The Python code below is the minimum code that is required in a submission file:
# 1. The "datamodel" imports at the top. Using the typing library is optional.
# 2. A class called "Trader", this class name should not be changed.
# 3. A run function that takes a tradingstate as input and outputs a "result" dict.

from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order, Trade
import numpy as np

expenditure = 0
gained = 0

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        result = {}
        
        print(state.toJSON())
        for product in state.order_depths.keys():
            if product == 'PEARLS':
                order_depth : OrderDepth = state.order_depths[product]
                orders : List[Order] = []
                market_trades : Trade = state.market_trades[product]
                # a fair value for pearls, calculate this afterwords
                # acceptable_price = 1
                acceptable_price = fair_value(market_trades)
                if len(order_depth.sell_orders) >0 :
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]


                if best_ask < acceptable_price :
                    print("BUY", str(-best_ask_volume)+ "x", best_ask)
                    orders.append(Order(product, best_ask,-best_ask_volume))

                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > acceptable_price:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))

                result[product] = orders

        return result


def fair_value(market_trades):
    prices = [trade.price for trade in market_trades]
    return np.average(prices)