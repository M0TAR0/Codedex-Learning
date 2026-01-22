#32. Stonks Program

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    price = stock_prices[x-1]
    return price

def max_price(a, b):
    max_price = max(stock_prices[a-1 : b])
    return max_price

def min_price(a, b):
    min_price = min(stock_prices[a-1 : b])
    return min_price

print(price_at(2))
print(max_price(2, 5))
print(min_price(2, 4))