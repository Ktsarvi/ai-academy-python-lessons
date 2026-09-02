from datetime import datetime
import json
from subscription import Subscription

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)

    def remove_subscription(self, name):
        for subscription in self.subscriptions:
            if subscription.name.lower() == name.lower():
                self.subscriptions.remove(subscription)
                return True

        return False

    def list_subscriptions(self):
        if not self.subscriptions:
            print("\nNo subscriptions found.")
            return

        print()
        for subscription in self.subscriptions:
            print(subscription)

    def monthly_cost(self):
        total = 0

        for subscription in self.subscriptions:
            if subscription.billing_cycle == "weekly":
                total += subscription.price * 52 / 12
            elif subscription.billing_cycle == "monthly":
                total += subscription.price
            elif subscription.billing_cycle == "yearly":
                total += subscription.price / 12

        return total

    def upcoming_payments(self):
        if not self.subscriptions:
            print("\nNo subscriptions found.")
            return
        print()

        today = datetime.today().date()

        payments = []

        for subscription in self.subscriptions:
            payment_date = datetime.strptime(
                subscription.next_payment,
                "%Y-%m-%d"
            ).date()

            days_left = (payment_date - today).days

            payments.append((subscription, payment_date, days_left))

        payments.sort(key=lambda x: x[1])

        for subscription, payment_date, days_left in payments:
            if days_left < 0:
                print(
                    f"{subscription.name} - "
                    f"overdue by {abs(days_left)} days"
                )
            elif days_left == 0:
                print(
                    f"{subscription.name} - "
                    f"payment is TODAY"
                )
            else:
                print(
                    f"{subscription.name} - "
                    f"{payment_date} - "
                    f"in {days_left} days"
                )

    def save_subscriptions(self):
        data = []

        for subscription in self.subscriptions:
            data.append({
                "name": subscription.name,
                "price": subscription.price,
                "billing_cycle": subscription.billing_cycle,
                "next_payment": subscription.next_payment
            })

        with open("subscriptions.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_subscriptions(self):
        try:
            with open("subscriptions.json", "r") as file:
                data = json.load(file)

            for item in data:
                subscription = Subscription(
                    item["name"],
                    item["price"],
                    item["billing_cycle"],
                    item["next_payment"]
                )

                self.subscriptions.append(subscription)

        except FileNotFoundError:
            pass
            
    def spending_statistics(self):
        if not self.subscriptions:
            print("\nNo subscriptions found.")
            return

        monthly = self.monthly_cost()
        yearly = monthly * 12
        weekly = monthly * 12 / 52

        weekly_subscriptions = 0
        monthly_subscriptions = 0
        yearly_subscriptions = 0

        for subscription in self.subscriptions:
            if subscription.billing_cycle == "weekly":
                weekly_subscriptions += 1
            elif subscription.billing_cycle == "monthly":
                monthly_subscriptions += 1
            elif subscription.billing_cycle == "yearly":
                yearly_subscriptions += 1

        def get_monthly_cost(subscription):
            if subscription.billing_cycle == "weekly":
                return subscription.price * 52 / 12
            elif subscription.billing_cycle == "monthly":
                return subscription.price
            elif subscription.billing_cycle == "yearly":
                return subscription.price / 12
            return 0

        most_expensive = max(
            self.subscriptions,
            key=get_monthly_cost
        )

        print("\nSPENDING STATISTICS")
        print(f"Weekly spending: {weekly:.2f} AZN")
        print(f"Monthly spending: {monthly:.2f} AZN")
        print(f"Yearly spending: {yearly:.2f} AZN")
        print(f"Weekly subscriptions: {weekly_subscriptions}")
        print(f"Monthly subscriptions: {monthly_subscriptions}")
        print(f"Yearly subscriptions: {yearly_subscriptions}")
        print(
            f"Most expensive: "
            f"{most_expensive.name} "
            f"({get_monthly_cost(most_expensive):.2f} AZN/month)"
        )

    def search_subscriptions(self, query):
        results = []

        for subscription in self.subscriptions:
            if query.lower() in subscription.name.lower():
                results.append(subscription)

        if not results:
            print("\nNo subscriptions found.")
            return
        print()

        for subscription in results:
            print(subscription)

    def show_warnings(self):
        if not self.subscriptions:
            return

        today = datetime.today().date()
        warnings = []

        for subscription in self.subscriptions:
            payment_date = datetime.strptime(
                subscription.next_payment,
                "%Y-%m-%d"
            ).date()

            days_left = (payment_date - today).days

            if days_left < 0:
                warnings.append(
                    f"{subscription.name} - "
                    f"OVERDUE by {abs(days_left)} days"
                )

            elif days_left == 0:
                warnings.append(
                    f"{subscription.name} - "
                    f"payment is TODAY"
                )

            elif days_left <= 7:
                warnings.append(
                    f"{subscription.name} - "
                    f"payment in {days_left} days"
                )

        if not warnings:
            return

        print("\nWARNINGS:")

        for warning in warnings:
            print(warning)
        print()