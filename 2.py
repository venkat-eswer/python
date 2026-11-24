print("lesson 2 which shows how to input the variables in python and conditions")

name = input("Enter your name :: ")
age = int(input("Enter your age :: "))
if age >= 21:
    print(f"Hello {name}, you are {age} years old and eligible to vote.")
elif age < 0:
    print(f"you entered a negative age, please enter a valid age.")
else:
    print(f"Hello {name}, you are {age} years old and not eligible to vote.")
