from limit_order_book.matching_engine import MatchingEngine
from limit_order_book.order import Side, Order


def test_buy_no_sellers():
    matching_engine = MatchingEngine()
    order = Order(1, Side.BUY, 100, 10)
    matching_engine.process_order(order)

    assert len(matching_engine.order_book.bids) == 1
    assert matching_engine.order_book.bids[order.price][0] == order

def test_sell_no_buyers():
    matching_engine = MatchingEngine()
    order = Order(1, Side.SELL, 100, 10)
    matching_engine.process_order(order)

    assert len(matching_engine.order_book.asks) == 1
    assert matching_engine.order_book.asks[order.price][0] == order

def test_engine_no_matches():
    matching_engine = MatchingEngine()
    order_1 = Order(1, Side.BUY, 100, 10)
    order_2 = Order(1, Side.SELL, 101, 10)
    matching_engine.process_order(order_1)
    matching_engine.process_order(order_2)

    assert len(matching_engine.order_book.bids) == 1
    assert matching_engine.order_book.bids[order_1.price][0] == order_1

    assert len(matching_engine.order_book.asks) == 1
    assert matching_engine.order_book.asks[order_2.price][0] == order_2

def test_engine_full_match():
    matching_engine = MatchingEngine()
    order_1 = Order(1, Side.BUY, 100, 10)
    order_2 = Order(1, Side.SELL, 99, 10)
    matching_engine.process_order(order_1)
    matching_engine.process_order(order_2)

    assert len(matching_engine.order_book.bids) == 0
    assert len(matching_engine.order_book.asks) == 0

def test_engine_resting_order():
    matching_engine = MatchingEngine()
    order_1 = Order(1, Side.BUY, 100, 5)
    order_2 = Order(1, Side.SELL, 99, 10)
    matching_engine.process_order(order_1)
    matching_engine.process_order(order_2)

    assert len(matching_engine.order_book.bids) == 0
    assert matching_engine.order_book.asks[order_2.price][0] == order_2
    assert len(matching_engine.order_book.asks) == 1

def test_engine_incoming_order():
    matching_engine = MatchingEngine()
    order_1 = Order(1, Side.BUY, 100, 15)
    order_2 = Order(1, Side.SELL, 99, 10)
    matching_engine.process_order(order_1)
    matching_engine.process_order(order_2)

    assert len(matching_engine.order_book.bids) == 1
    assert matching_engine.order_book.bids[order_1.price][0] == order_1
    assert len(matching_engine.order_book.asks) == 0

def test_engine_multiple_resting_order():
    matching_engine = MatchingEngine()
    order_1 = Order(1, Side.BUY, 100, 2)
    order_2 = Order(1, Side.BUY, 100, 2)
    order_3 = Order(1, Side.BUY, 100, 2)
    order_4 = Order(1, Side.SELL, 99, 8)
    matching_engine.process_order(order_1)
    matching_engine.process_order(order_2)
    matching_engine.process_order(order_3)
    matching_engine.process_order(order_4)

    assert len(matching_engine.order_book.bids) == 0
    assert matching_engine.order_book.asks[order_4.price][0] == order_4
    assert len(matching_engine.order_book.asks) == 1

def test_engine_trades():
    matching_engine = MatchingEngine()
    order_1 = Order(1, Side.SELL, 100, 5)
    order_2 = Order(1, Side.BUY, 105, 5)
    matching_engine.process_order(order_1)
    matching_engine.process_order(order_2)

    assert len(matching_engine.trades) == 1
    assert matching_engine.trades[0].buy_order_id == order_1.order_id
    assert matching_engine.trades[0].sell_order_id == order_2.order_id







