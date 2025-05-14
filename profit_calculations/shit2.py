# Define your trades as a list of tuples: (price_bought, amount_bought)
trades = [
    (12.5, 296),  # Example: bought 100 shares at $10.50
    (11.9, 441),   # bought 50 shares at $12.30
    (8.6, 1045),   # and so on...
    (8.7, 260),
]

def calc_profit(entry_price, exit_price, amount, leverage):
    return (exit_price - entry_price) * amount * leverage

tot_profit = 0
out_price = 17.00
l = 5
for trade in trades:
    tot_profit += calc_profit(trade[0], out_price, trade[1], l)
print(tot_profit)

# Here is just a test:

print("Now testing...")

prof = calc_profit(1, 2, 10, 2) # out price is just 2, in price is 1, amount is 10, therefore you control 20 and it doubles so profit should be 20
print(prof)


'''
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

'''
