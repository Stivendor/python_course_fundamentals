# builtin modules in python for file handling 

# if we need to delay the execution of a program we can use the time module
import time
print("program starts")

with open("../files/delay.txt","w") as file:
    file.write("This file was created after a delay.\n")
    time.sleep(3)  # delay for 3 seconds
    file.write("File creation completed after delay.\n")
print("File created after delay.")

# if we want to print line by line with a delay
print("Reading file with delay:")
with open("../files/fruits.txt","r") as file:
    for line in file: 
        print(line.strip()) # strip() to remove extra newlines
        time.sleep(1)  # delay for 1 second between lines

# we can import os module to work with file paths
import os # os module provides functions to interact with the operating system
import time # time module to add delay

print("Checking for the existence of vegetables.txt every 5 seconds:")
while True:
    if os.path.exists("../files/vegetables.txt"):
        with open("../files/vegetables.txt", "r") as file:
            content = file.read()
        print("File found. Here is the content:")
        print(content)
    else:
        print("File not found. Please check the path.")
    time.sleep(5)  # wait for 10 seconds before checking again