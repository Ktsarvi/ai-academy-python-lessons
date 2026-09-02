from datetime import datetime

def get_valid_name():
    while True:
        name = input("Subscription name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")

def get_valid_price():
    while True:
        try:
            price = float(input("Price: "))

            if price <= 0:
                print("Price must be greater than 0.")
                continue

            return price

        except ValueError:
            print("Please enter a valid number.")

def get_valid_billing_cycle():
    while True:
        billing_cycle = input(
            "Billing cycle (weekly/monthly/yearly): "
        ).strip().lower()

        if billing_cycle in ("weekly", "monthly", "yearly"):
            return billing_cycle

        print("Billing cycle must be weekly, monthly, or yearly.")

def get_valid_date():
    while True:
        date = input("Next payment (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")