# I will try to make this exercise only knowing the output of the solution that it's the next:

# Say something : its a good weather today
# Say something : how its the weather there
# Say something : theres only some clouds here     
# It's a good weather today. How its the weather there?. there's only some clouds here.

# This function helps us to convert a phrase in lowercase into a capitalized phrase
def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how","why", "what")
    if phrase.startswith(interrogatives):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

results = []
while True: 
    user_input = input("Say something : ")
    if user_input == "exit": 
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))

# This is another exercise given by gemini

# Enter a number (or 'done' to stop): 10
# Current Average: 10.0
# Enter a number (or 'done' to stop): 20
# Current Average: 15.0
# Enter a number (or 'done' to stop): done
# --- Results ---
# Numbers Entered: [10.0, 20.0]
# Final Average: 15.00

def calculate_average(numbers):
    if not numbers:
        return 0.0
    
    return sum(numbers) / len(numbers)

number_list = []
while True:
    user_input = input("Enter a number (or 'done' to stop): ")
    if user_input == "done": 
        break
    else: 
        numbers = float(user_input)
        number_list.append(numbers)
        current_average = calculate_average(number_list)
        print(f"Current average: {current_average:1f}")

print(f"Numbers entered: {number_list}")
print(f"Final average: {calculate_average(number_list)}" )