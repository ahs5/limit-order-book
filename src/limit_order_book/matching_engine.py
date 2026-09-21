from limit_order_book.order import Side
from limit_order_book.order_book import OrderBook


class MatchingEngine:
    def __init__(self):
        self.order_book = OrderBook()

    def process_order(self, order):
        while order.remaining_quantity > 0:
            if order.side == Side.BUY:
                if len(self.order_book.asks) == 0:
                    self.order_book.add_order(order)
                    return
                elif self.order_book.best_ask().price > order.price:
                    self.order_book.add_order(order)
                    return
                else:
                    resting_order = self.order_book.best_ask()
                    trade_quantity = min(
                        order.remaining_quantity,
                        resting_order.remaining_quantity
                    )
                    order.fill_order(trade_quantity)
                    resting_order.fill_order(trade_quantity)
                    if resting_order.remaining_quantity == 0:
                        self.order_book.pop_best_ask()
            elif order.side == Side.SELL:
                if len(self.order_book.bids) == 0:
                    self.order_book.add_order(order)
                    return
                elif self.order_book.best_bid().price < order.price:
                    self.order_book.add_order(order)
                    return
                else:
                    resting_order = self.order_book.best_bid()
                    trade_quantity = min(
                        order.remaining_quantity,
                        resting_order.remaining_quantity
                    )
                    order.fill_order(trade_quantity)
                    resting_order.fill_order(trade_quantity)
                    if resting_order.remaining_quantity == 0:
                        self.order_book.pop_best_bid()
            else:
                raise ValueError("invalid order side")