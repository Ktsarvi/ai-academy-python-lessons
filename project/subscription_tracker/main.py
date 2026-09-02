from subscription import Subscription
from manager import SubscriptionManager


manager = SubscriptionManager()

spotify = Subscription(
    "Spotify",
    5.99,
    "monthly",
    "2026-09-15"
)

netflix = Subscription(
    "Netflix",
    15.99,
    "monthly",
    "2026-09-10"
)

github = Subscription(
    "GitHub",
    48,
    "yearly",
    "2027-01-20"
)

manager.add_subscription(spotify)
manager.add_subscription(netflix)
manager.add_subscription(github)

print("\n" + "Your subscriptions:" + "\n")

manager.list_subscriptions()

print(f"\nMonthly cost: {manager.monthly_cost():.2f} AZN")
print(f"Yearly cost: {manager.yearly_cost():.2f} AZN")