from limit_order_book.order import Order, Side
from limit_order_book.order_book import OrderBook
import pytest

def test_buy():
    order = Order(1, Side.BUY, 100, 10)
    order_book = OrderBook()
    order_book.add_order(order)

    assert order_book.bids[100][0] == order
    assert len(order_book.bids[100]) == 1

def test_sell():
    order = Order(1, Side.SELL, 100, 10)
    order_book = OrderBook()
    order_book.add_order(order)

    assert order_book.asks[100][0] == order
    assert len(order_book.asks[100]) == 1

def test_multiple_buy():
    order_1 = Order(1, Side.BUY, 100, 10)
    order_2 = Order(2, Side.BUY, 100, 10)
    order_book = OrderBook()
    order_book.add_order(order_1)
    order_book.add_order(order_2)

    assert order_book.bids[100][0] == order_1
    assert order_book.bids[100][1] == order_2
    assert len(order_book.bids[100]) == 2

def test_multiple_priced_buy():
    order_1 = Order(1, Side.BUY, 100, 10)
    order_2 = Order(2, Side.BUY, 101, 10)
    order_book = OrderBook()
    order_book.add_order(order_1)
    order_book.add_order(order_2)

    assert order_book.bids[100][0] == order_1
    assert order_book.bids[101][0] == order_2
    assert len(order_book.bids) == 2

def test_best_bid():
    order_1 = Order(1, Side.BUY, 99, 10)
    order_2 = Order(2, Side.BUY, 100, 10)
    order_3 = Order(3, Side.BUY, 101, 10)
    order_book = OrderBook()
    order_book.add_order(order_1)
    order_book.add_order(order_2)
    order_book.add_order(order_3)

    assert order_book.best_bid() == order_3


def test_best_ask():
    order_1 = Order(1, Side.SELL, 99, 10)
    order_2 = Order(2, Side.SELL, 100, 10)
    order_3 = Order(3, Side.SELL, 101, 10)
    order_book = OrderBook()
    order_book.add_order(order_1)
    order_book.add_order(order_2)
    order_book.add_order(order_3)

    assert order_book.best_ask() == order_1

def test_best_bid_same_bid():
    order_1 = Order(1, Side.BUY, 100, 10)
    order_2 = Order(2, Side.BUY, 100, 10)
    order_book = OrderBook()
    order_book.add_order(order_1)
    order_book.add_order(order_2)

    assert order_book.best_bid() == order_1

def test_best_bid_none_bid():
    order_book = OrderBook()

    assert order_book.best_bid() is None

def test_best_ask_none_ask():
    order_book = OrderBook()

    assert order_book.best_ask() is None