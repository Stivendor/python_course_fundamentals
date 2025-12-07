# using with statement to read a file is the best practice because
# it automatically handles closing the file after its suite finishes.


# if we have the file in another directory we can specify the path
with open("../files/fruits.txt", "r") as file:
    # read the content of the file
    content = file.read()
print(content)

# write mode
with open("../files/vegetables.txt", "w") as file:
    # write some content to the file
    file.write("Carrot\nOnion\nCabbage\n")
    file.write("Spinach\nPotato\n")
    
print("Vegetables written to the file:")
# read mode
with open("../files/vegetables.txt", "r") as file:
    # read the content of the file
    content = file.read()
print(content)

# append mode to add more content without overwriting
print("More vegetables appended to the file:")
with open("../files/vegetables.txt", "a+") as file: # a+ mode opens the file for both appending and reading
    file.write("Tomato\nCucumber\n")
    file.seek(0)  # move the cursor to the beginning of the file
    content = file.read()
print(content)



