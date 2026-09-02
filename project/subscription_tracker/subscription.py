class Subscription:
    def __init__(self, name, price, billing_cycle, next_payment):
        self.name = name
        self.price = price
        self.billing_cycle = billing_cycle
        self.next_payment = next_payment

    def monthly_cost(self):
        if self.billing_cycle == "weekly":
            return self.price * 52 / 12

        elif self.billing_cycle == "monthly":
            return self.price

        elif self.billing_cycle == "yearly":
            return self.price / 12

        return 0

    def __str__(self):
        return f"{self.name} - {self.price:.2f} AZN ({self.billing_cycle})"