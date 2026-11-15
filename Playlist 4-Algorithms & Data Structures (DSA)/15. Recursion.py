#Recursion:programming technique where a function calls itself directly or indirectly to solve a subproblem
#It needs a base case and recursive case
#Base case:act as a stopping condition that prevents infinite recursion
#Recursive case:The block of code that does recursion
#Call stack:A system-level data structure that keeps track of the active function calls in a program. Each recursive call adds a new stack frame which included Function parameters, local variables, and the return address to the top.
#Call Stack in python limits how many times a function can stack on top of itself to protect your computer's memory.

def countdown():
    print("Counting down...")
countdown()

#Correct code
def countdown2(number):
    #1. Base case
    if number == 0:
        return

    #2.Recursive case
    print(number)
    countdown2(number - 1)
#Calling function
countdown2(5)


def factorial(number):
    #Base case
    if number<=1:
        return 1
    #Recursive case
    return number * factorial(number - 1)

print(factorial(3))

