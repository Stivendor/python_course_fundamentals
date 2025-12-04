# Tuples are similar to lists, but they are immutable, meaning their content cannot be changed after creation.
students_grades = (1,2,3,4,5)
print(students_grades)
#print(students_grades.remove(3)) # This will raise an AttributeError because tuples do not have an append method.

# Tuples have some methods that cam be used to perform operations on the tuple
# we can ssaw the methods using the dir() function
print(dir(students_grades))




