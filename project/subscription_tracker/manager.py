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
            print("No subscriptions found.")
            return

        for subscription in self.subscriptions:
            print(subscription)

    def monthly_cost(self):
        total = 0

        for subscription in self.subscriptions:
            if subscription.billing_cycle == "monthly":
                total += subscription.price
            elif subscription.billing_cycle == "yearly":
                total += subscription.price / 12

        return total

    def yearly_cost(self):
        return self.monthly_cost() * 12