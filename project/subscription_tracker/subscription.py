class Subscription:
    def __init__(self, name, price, billing_cycle, next_payment):
        self.name = name
        self.price = price
        self.billing_cycle = billing_cycle
        self.next_payment = next_payment

    def __str__(self):
        return f"{self.name} - {self.price} AZN ({self.billing_cycle})"

subscription = Subscription(
    "Spotify",
    5.99,
    "monthly",
    "2026-09-15"
)
print(subscription)