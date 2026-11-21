prices = [120, 250, 180, 400, 150, 300, 500, 220, 350, 100]

average = sum(prices) / len(prices)

result = [price for price in prices if price > average]

print("Average price:", average)
print("Prices above average:", result)