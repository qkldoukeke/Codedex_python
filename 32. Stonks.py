# Write code below 💖

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
  mx = 0
  if a < 1 or b > 20:
    print("error!")
  else:
    for i in range(a-1,b):
      mx = max(mx, stock_prices[i])
    return mx

def min_price(a, b):
  mn = 60;
  if a < 1 or b > 20:
    print("error!")
  else:
    for i in range(a-1,b):
      mn = min(mn, stock_prices[i])
    return mn

print(max_price(3, 4))
print(min_price(3, 4))
print(price_at(2))