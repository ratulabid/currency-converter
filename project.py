# Exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.91,
    "GBP": 0.77,
    "BDT": 119.05,
    "INR": 83.22,
    "JPY": 145.32
}

# Currency symbols
currency_symbols = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "BDT": "৳",
    "INR": "₹",
    "JPY": "¥"
}

print("Welcome to the Currency Converter!")
print("Available currencies:", ", ".join(exchange_rates.keys()))

# Loop for multiple conversions
while True:
    # Get and validate amount input
    while True:
        amount_input = input("\nEnter amount: ")
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("❌ Amount must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

    # Get and validate currency codes
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("❌ Invalid currency code! Please try again.")
    else:
        # Convert to USD first, then to target currency
        amount_in_usd = amount / exchange_rates[from_currency]
        converted_amount = amount_in_usd * exchange_rates[to_currency]

        from_symbol = currency_symbols.get(from_currency, "")
        to_symbol = currency_symbols.get(to_currency, "")

        # Show result
        print(f"\n✅ {from_symbol}{amount:,.2f} {from_currency} = {to_symbol}{converted_amount:,.2f} {to_currency}")

    # Ask if the user wants to convert another amount
    again = input("\nDo you want to convert another amount? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for using the Currency Converter! 👋")
        break
