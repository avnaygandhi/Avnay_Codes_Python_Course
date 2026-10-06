#Functions:reusable block of executable code
#Parameter: the placeholder inside the function definition.
#Argument: the actual data passed when calling the function which is the stored value in parameter name.
def greet():
    print("Welcome back to Avnay Codes!")
greet()

name_input = input("What is your name? ")
#1.
def greet_user(name):
    print(f"Welcome {name} back to Avnay Codes!")
greet_user(name_input)

#2.
def greet_user(name=name_input):
    print(f"Welcome {name} back to Avnay Codes!")
greet_user()

greet_user(name=name_input)
