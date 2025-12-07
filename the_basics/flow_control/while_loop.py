# while loop in python is used to repeatedly execute a block of code as long as a given condition is true.
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # increment count by 1
print("Finished counting!")

username = ""
while username != "admin":
    username = input("Enter username (type 'admin' to exit): ")
    print(f"Hello, {username}!")
print("Welcome, admin!")

# the most common way to use while loop it's using a break statement and continue statement
while True:
    password = input("Enter password (type 'exit' to quit): ")
    if password == "exit":
        print("exiting...")
        break  # exit the loop
    if len(password) < 6:
        print("Password too short, try again.")
        continue  # skip the rest of the loop and start from the beginning
    print("Password accepted!")

# using while loop to calculate the factorial of a number
number = int(input("Enter a positive integer to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i  # multiply factorial by i
    i += 1  # increment i by 1
print(f"The factorial of {number} is {factorial}")


