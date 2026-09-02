class Subscription:
    def __init__(self, name, price, billing_cycle, next_payment):
        self.name = name
        self.price = price
        self.billing_cycle = billing_cycle
        self.next_payment = next_payment

    def __str__(self):
        return f"{self.name} - {self.price:.2f} AZN ({self.billing_cycle})"