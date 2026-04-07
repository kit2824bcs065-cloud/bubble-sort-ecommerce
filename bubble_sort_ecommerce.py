 Bubble Sort - E-commerce Product Price Sorting

prices = [1200, 800, 1500, 500]

n = len(prices)

Bubble Sort Logic
for i in range(n - 1):
    for j in range(n - i - 1):
        if prices[j] > prices[j + 1]:
            swap
            temp = prices[j]
            prices[j] = prices[j + 1]
            prices[j + 1] = temp

Output
print("Sorted Prices (Low to High):")
for price in prices:
    print("₹", price)
