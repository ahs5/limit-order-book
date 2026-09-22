# limit order book
A python implementation of a limit order book and matching engine using price time priority

## features
- buy and sell limit orders
- price time priority
- partial fills
- orders matching across multiple price levels
- trade recording
- command line interface
- pytest test suite

## project structure 
```text
src/limit_order_book/
    __init__.py
    order.py
    order_book.py
    matching_engine.py
    trade.py
    __main__.py

tests/
    test_matching_engine.py
    test_order.py
    test_order_book.py
```
## matching engine rules
- highest bid has priority
- lowest ask has priority
- FIFO within the same price level
- incoming BUY matches asks at or below its limit
- incoming sell matches bids at or above its limit
- execution occurs at the resting order's price

## running
cd src
python -m limit_order_book

## testing
pytest
