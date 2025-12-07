# List comprehension are a concise way to create lists.
# next we will see some examples an differences between traditional for loops and list comprehensions.

temps = [221, 234, 340, 230, -9999]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
print(new_temps)  # this is the traditional way using for loops

new_temps_comprehension = [temp / 10 for temp in temps]
print(new_temps_comprehension)  # this is the same using list comprehension

# we can also add conditions to list comprehensions
new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)  # this will exclude the -9999 value



# we can do also functions inside list comprehensions
def foo(lst):
    return [i for i in lst if i % 2 == 0]
print(foo(range(10)))  # this will print only the even numbers from 0 to 9
