# Dictionaries are unordered collections of key-value pairs
# in this case, the key are the names and the value are the grades
students_grades = {"Stiven": 4, "Maria": 5, "Julian": 4}

# with the .keys we can get the names of the keys in the dictionary
print(students_grades.keys())

# with the .values we can get the values of the dictionary
print(students_grades.values())

# to acces a value in the dictionary we use the key
print(students_grades["Maria"])
# it's useful because if for example we have a dictionary with countries and their capitals, we can do this:
countries_capitals = {"Colombia": "Bogota", "France": "Paris", "Japan": "Tokyo"}
print(countries_capitals["Japan"])

