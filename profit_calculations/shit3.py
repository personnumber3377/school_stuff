# Your trades
trades = [
    (12.5, 296),
    (11.9, 441),
    (8.6, 1045),
    (8.7, 260),
]

leverage = 5
current_price = 16.88  # Current SOXL price

total_shares = 0
total_cost = 0.0

for buy_price, amount in trades:
    total_shares += amount
    total_cost += buy_price * amount

# Total position value at current price
current_value = total_shares * current_price

# Borrowed money = 4/5 of the cost (assuming 5x leverage)
borrowed_amount = (leverage - 1) / leverage * total_cost

# Equity is what you'd be left with after repaying the borrowed amount
equity = current_value - borrowed_amount

# Optional: also show your original capital
capital_invested = total_cost / leverage

# Print results
print(f"Total shares: {total_shares}")
print(f"Total cost (unleveraged): €{total_cost:.2f}")
print(f"Capital invested: €{capital_invested:.2f}")
print(f"Borrowed amount: €{borrowed_amount:.2f}")
print(f"Current value of position: €{current_value:.2f}")
print(f"Your equity (if you sell all now): €{equity:.2f}")
print(f"Total gain: €{equity - capital_invested:.2f}")
print(f"Return on capital: {(equity / capital_invested) * 100:.2f}%")
