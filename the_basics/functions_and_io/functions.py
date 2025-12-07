# Functions in python are defined using the def keyword
def average(numbers):
    return sum(numbers) / len(numbers)
grades = [2.2, 4, 4.6]
print(average(grades))


# Function with multiple parameters
def convert_money(amount, rate):
    return amount * rate
dollars = 100
exchange_rate = 3.8
print(convert_money(dollars, exchange_rate))

def triangle_area(base, height):
    return (base * height) / 2
print(triangle_area(1, 1))

## Default parametrer value
def circle_area(radius, pi=3.1415):
    return f"{(radius * pi):1f}"
print(circle_area(5))

# Using *args to pass a variable number of arguments to a function
def average_var_args(*args):
    return sum(args) / len(args)
print(average_var_args(2.2, 4, 4.6, 5, 3.8))

# Using **kwargs to pass a variable number of keyword arguments to a function
def print_user_info(**kwargs):
    return kwargs

print(print_user_info(name="John", age=30, city="New York"))