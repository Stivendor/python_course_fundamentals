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

