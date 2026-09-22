from limit_order_book.matching_engine import MatchingEngine
from limit_order_book.order import Order, Side


def mian():
    matching_engine = MatchingEngine()
    order_id = 1
    while True:
        num_of_trades = len(matching_engine.trades)
        side_input = input("Enter the order side (BUY or SELL): ").strip().upper()
        side = Side(side_input)
        price = int(input("Enter the order price: "))
        quantity = int(input("Enter the order quantity: "))
        order = Order(order_id, side, price, quantity)
        matching_engine.process_order(order)
        if len(matching_engine.trades) != num_of_trades:
            for trade in matching_engine.trades[num_of_trades:]:
                print(
                    f"Trade executed: BUY order ID: {trade.buy_order_id}"
                    f" SELL order ID: {trade.sell_order_id}"
                    f" Price: {trade.price}"
                    f" Quantity: {trade.quantity}"
                )

        order_id += 1
        status = input("enter q to exit or press enter to continue: ")
        if status == "q":
            break
        else:
            continue


if __name__ == '__main__':
    mian()

