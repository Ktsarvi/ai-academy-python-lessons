import requests

response = requests.post


# class InsufficientFundsError(Exception):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

# def add_item(item, bucket=[]): 
#     bucket.append(item) 
#     return bucket

# def outer_wrapper(func):
#     def inner_wrapper():
#         print("log 1")
#         func()
#         print("log 2")
#     return inner_wrapper

# @outer_wrapper
# def my_function():
#     print("my function")

# my_function()
