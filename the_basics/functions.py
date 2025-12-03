# Functions in python are defined using the def keyword
def average(numbers):
    return sum(numbers) / len(numbers)
grades = [2.2, 4, 4.6]
print(average(grades))

def convert_money(amount, rate):
    return amount * rate
dollars = 100
exchange_rate = 3.8
print(convert_money(dollars, exchange_rate))