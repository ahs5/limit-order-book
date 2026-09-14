from limit_order_book.order import Order, Side
import pytest

def test_create_order():
    order = Order(1, Side.BUY, 100, 10)

    assert order.order_id == 1
    assert order.side == Side.BUY
    assert order.price == 100
    assert order.quantity == 10
    assert order.remaining_quantity == 10
    assert order.timestamp is None

def test_partial_order():
    order = Order(1, Side.BUY, 100, 10)
    order.fill_order(3)
    assert order.remaining_quantity == 7
    assert order.quantity == 10

def test_full_fill_order():
    order = Order(1, Side.BUY, 100, 10)
    order.fill_order(10)
    assert order.remaining_quantity == 0
    assert order.quantity == 10

def test_zero_fill_order():
    order = Order(1, Side.BUY, 100, 10)

    with pytest.raises(ValueError):
        order.fill_order(0)

def test_negative_fill_order():
    order = Order(1, Side.BUY, 100, 10)

    with pytest.raises(ValueError):
        order.fill_order(-1)

def test_overfill_order():
    order = Order(1, Side.BUY, 100, 10)

    with pytest.raises(ValueError):
        order.fill_order(11)
