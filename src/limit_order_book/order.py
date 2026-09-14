from enum import Enum

class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order:
    def __init__(self, order_id, side, price, quantity):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.remaining_quantity = quantity
        self.timestamp = None

    def fill_order(self, fill_quantity):
        if 0 < fill_quantity <= self.remaining_quantity:
            self.remaining_quantity -= fill_quantity
        elif fill_quantity <= 0:
            raise ValueError("quantity must be greater than 0")
        elif fill_quantity > self.remaining_quantity:
            raise ValueError("quantity must be less than remaining quantity")