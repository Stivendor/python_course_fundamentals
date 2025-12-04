# for loops are one of the most common ways to iterate over a sequence (list, tuple, string) or other iterable objects in Python.
# If we have a list of student grades and we want to round each grade to the nearest integer, we can use a for loop to 
# iterate over the list and apply the round function to each grade.
student_grades_list = [2.2, 5, 4.7, 3.3, 4.9]
print(round(student_grades_list[0])) # this is the slow way to round each grade

for grade in student_grades_list:
    print(round(grade))  # this is the fast way using a for loop

print()

# We can also use for loops to iterate over strings
student_name = "Stiven"
for letter in student_name:
    print(letter)

# If we have a dictionary of student grades, we can use a for loop to iterate over the keys and values of the dictionary.
student_grades_list_dict = {'math': 4.6, 'science': 3.8, 'literature': 4.0}

# Iterating over the items (key-value pairs) of the dictionary
for subject in student_grades_list_dict.items():
    print(subject)  # this will print the key-value pairs as tuples

# Iterating over the keys of the dictionary
for subject in student_grades_list_dict.keys():
    print(subject)  # this will print only the keys

# Iterating over the values of the dictionary
for grade in student_grades_list_dict.values():
    print(grade)  # this will print only the values

# Dictionary loop and string fromatting
for subject, grade in student_grades_list_dict.items():
    print(f"The grade in {subject} is {grade}")  # formatted string to print the subject and grade
