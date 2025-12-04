# From tuple to a list
students_grades = (1, 2, 3, 4, 5)
print(students_grades)
students_grades_list = list(students_grades) # converting the tuple to a list
print(students_grades_list)

# From list to a tuple
students_grades = [1, 2, 3, 4, 5]  
print(students_grades)
students_grades_tuple = tuple(students_grades) # converting the list to a tuple
print(students_grades_tuple)

# From string to a list
student_name = "Stiven"
print(student_name)
student_name_list = list(student_name) # converting the string to a list
print(student_name_list)

# From list to a string
student_name_list = ['S', 't', 'i', 'v', 'e', 'n']
print(student_name_list)
student_name = str.join("",student_name_list) # converting the list to a string
print(student_name)