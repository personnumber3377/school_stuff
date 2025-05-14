# Define your trades as a list of tuples: (price_bought, amount_bought)
trades = [
    (12.5, 296),  # Example: bought 100 shares at $10.50
    (11.9, 441),   # bought 50 shares at $12.30
    (8.6, 1045),   # and so on...
    (8.7, 260),
]

leverage = 5
sell_price = 16.83

capital_invested = 0.0
leveraged_profit = 0.0

print("Trade breakdown:\n")

for buy_price, amount in trades:
    cost = buy_price * amount
    capital = cost / leverage
    profit = (sell_price - buy_price) * amount * leverage

    capital_invested += capital
    leveraged_profit += profit

    print(f"Bought {amount} @ €{buy_price:.2f}")
    print(f"  → Cost: €{cost:.2f}")
    print(f"  → Capital used: €{capital:.2f}")
    print(f"  → Leveraged profit: €{profit:.2f}")
    print()

print("\n--- Summary ---")
print(f"Total capital invested: €{capital_invested:.2f}")
print(f"Total leveraged profit: €{leveraged_profit:.2f}")
print(f"Return on capital: {(leveraged_profit / capital_invested) * 100:.2f}%")


