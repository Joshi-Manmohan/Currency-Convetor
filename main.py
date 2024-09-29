def currency_converter():
    # Predefined exchange rates
    rates = {
        "USD": 1.0,   # Base currency
        "EUR": 0.84,
        "GBP": 0.75,
        "JPY": 110.0,
        "INR": 74.0,  # Example rate: 1 USD = 74 INR
    }

    print("Welcome to the Currency Converter!")
    print("Available currencies: USD, EUR, GBP, JPY, INR")
    
    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., INR): ").upper()
    amount = float(input("Enter the amount: "))

    if from_currency in rates and to_currency in rates:
        # Convert to base currency (USD)
        amount_in_usd = amount / rates[from_currency]
        # Convert from base currency to target currency
        converted_amount = amount_in_usd * rates[to_currency]
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency entered.")

if __name__ == "__main__":
    currency_converter()
