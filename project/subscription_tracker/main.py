from subscription import Subscription
from manager import SubscriptionManager
from utils import *

manager = SubscriptionManager()
manager.load_subscriptions()
manager.show_warnings()

while True:
    print("\nSUBSCRIPTION TRACKER")
    print("1. Add subscription")
    print("2. Remove subscription")
    print("3. Show subscriptions")
    print("4. Show monthly cost")
    print("5. Show yearly cost")
    print("6. Upcoming payments")
    print("7. Spending statistics")
    print("8. Search subscriptions")
    print("9. Save subscriptions")
    print("10. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = get_valid_name()
        price = get_valid_price()
        billing_cycle = get_valid_billing_cycle()
        next_payment = get_valid_date()

        subscription = Subscription(
            name,
            price,
            billing_cycle,
            next_payment
        )

        manager.add_subscription(subscription)

        print("Subscription added!")

    elif choice == "2":
        name = get_valid_name()

        if manager.remove_subscription(name):
            print("Subscription removed!")
        else:
            print("Subscription not found.")

    elif choice == "3":
        manager.list_subscriptions()

    elif choice == "4":
        print(f"Monthly cost: {manager.monthly_cost():.2f} AZN")

    elif choice == "5":
        print(f"Yearly cost: {manager.yearly_cost():.2f} AZN")

    elif choice == "6":
        manager.upcoming_payments()

    elif choice == "7":
        manager.spending_statistics()

    elif choice == "8":
        query = input("Search: ").strip()
        manager.search_subscriptions(query)

    elif choice == "9":
        manager.save_subscriptions()
        print("Subscriptions saved!")

    elif choice == "10":
        manager.save_subscriptions()
        print("Subscriptions saved!")
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-10.")