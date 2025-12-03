# Lists are ordered collections of items that can be of different data types 
students_grades = [1, 2, 3, 4, 5]
print(students_grades)

## the list can be of different data types
students_grades = ["John", 1, 2, 3, 4, 5]
print(students_grades)

## it also exists the range function that generates a sequence of numbers
students_grades = list(range(0, 5, 2)) # the number 2 is the step, so it will generate 0, 2, 4
print(students_grades)

# Average of a list of numbers, in this case the list is students_grades
student_grades = [2.2, 5, 4.7]
# the lists have methods that can be used to perform operations on the list
average = sum(student_grades) / len(student_grades)
print(average)
# sum = sum(list) with this we can sum all the numbers in the list
# len = len(list) with this we can get the length of a list

# Maximum and minimun value of a list of numbers
max_value = max(student_grades)
print(max_value)
min_value = min(student_grades)
print(min_value)

# Count the number of times a value appears in a list
count = student_grades.count(2.2)
print(count)

# Remove an item from a list
student_grades.remove(5)
print(student_grades)

# Add an item to a list
student_grades.append(3.8)
print(student_grades)

# Sort a list
student_grades.sort()
print(student_grades)

# Clear a list
student_grades.clear()
print(student_grades)

students_grades = [1, 2, 3, 4, 5]
# Index of an item in a list, for example, to find the index of the number 3
index_of_3 = students_grades.index(3, 0, 5)  # number to find=3, start=0, end=5 
print(index_of_3)

# __getitem__ method allows us to acssess an item in a list using the index
print(students_grades.__getitem__(2)) # this will print the item at index 2, which is 3
## another way more common to access an item in a list is using square brackets
print(students_grades[2]) # this will also print the item at index 2, which is 3 

# we can access to portions of a list using slicing
print(students_grades[1:4]) # this will print the items from index 1 to index 3, which are [2, 3, 4]
print(students_grades[:3])  # this will print the items from the start to index 2, which are [1, 2, 3]
print(students_grades[2:])  # this will print the items from index 2 to the end, which are [3, 4, 5] 
print(students_grades[-1]) # this will print the last item in the list, which is 5

# we can use strings aswell in lists and acces their characters using indexing
mystring = "Hello"
print(mystring[1]) # this will print the character at index 1, which is 'e'

data = ["Hello", 123, 45.67, True]
print(data[0][3]) # this will print the character at index 3 of the string at index 0 in the list, which is 'l'
print(data[0][-1]) # this will print the last character of the string at index 0 in the list, which is 'o'
print(data[0][:2]) # this will print the first two characters of the string at index 0 in the list, which is 'He'
print(data[0][2:]) # this will print the characters from index 2 to the end of the string at index 0 in the list, which is 'llo'