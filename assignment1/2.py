def maxProfit(A):
    max_profit = 0
    min_price = float('inf')
    
    for price in A:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit

# Example Input 1:
A1 = [1, 2]
print(maxProfit(A1))  # Output 1

# Example Input 2:
A2 = [1, 4, 5, 2, 4]
print(maxProfit(A2))  # Output 2
