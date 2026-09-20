from collections import deque
from limit_order_book.order import Side


class OrderBook:
    def __init__(self):
        self.bids = dict()
        self.asks = dict()

    def add_order(self, order):
        if order.side == Side.BUY:
            if order.price in self.bids:
                self.bids[order.price].append(order)
            else:
                self.bids[order.price] = deque([order])
        elif order.side == Side.SELL:
            if order.price in self.asks:
                self.asks[order.price].append(order)
            else:
                self.asks[order.price] = deque([order])
        else:
            raise ValueError("order side must be BUY or SELL")

    def best_bid(self):
        if self.bids:
            return self.bids[(max(self.bids))][0]
        else:
            return None

    def best_ask(self):
        if self.asks:
            return self.asks[(min(self.asks))][0]
        else:
            return None

    def pop_best_bid(self):
        if len(self.bids) == 0:
            return None
        else:
            best_price = max(self.bids)
            removed_order = self.bids[best_price].popleft()
            if len(self.bids[best_price]) == 0:
                self.bids.pop(best_price)
            return removed_order


    def pop_best_ask(self):
        if len(self.asks) == 0:
            return None
        else:
            best_price = min(self.asks)
            removed_order = self.asks[best_price].popleft()
            if len(self.asks[best_price]) == 0:
                self.asks.pop(best_price)
            return removed_order
