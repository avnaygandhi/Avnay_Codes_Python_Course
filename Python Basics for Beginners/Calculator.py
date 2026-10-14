# Smart Python Calculator
#1.Accept two number
#def add(a, b):
    #"""Adding two numbers"""
   # return a + b

#2. Allow any number of number
def add(*numbers):
    """Adding all the numbers """
    return sum(numbers)
def subtract(*numbers):
    """Subtracting all the numbers """
    if not numbers:
        return 0
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result
def multiply(*numbers):
    """Multiplying all the numbers """
    if not numbers:
        return 0
    result = numbers[0]
    for number in numbers[1:]:
        result *= number# result=result*number
    return result
def divide(*numbers):
    """Divides the first number by subsequent numbers"""
    if not numbers:
        return 0
    result = numbers[0]
    for number in numbers[1:]:
        try:
            result/=number
        except ZeroDivisionError:
            print("Division by zero not possible")
    return result

def show_history(history):
    """Shows the history of the calculation"""
    if not history:
        print("No history")
    else:
        print("\n Calculation history:")
        for idx, number in enumerate(history,1):
            print(f"{idx}. {number}")

def main():
    history = [] #list to show history
    print("Welcome to smart Python Calculator")
    while True:
        print("\n options:(+,-,*,/)|'h' for history or 'q' to quit")
        operation = input("Chose an operation: ").strip().lower()
        if operation == "h":
            show_history(history)
            continue
        elif operation == "q":
            print("Thank you for using smart Python Calculator")
            break
        elif operation not in ("+", "-", "*", "/"):
            print("Invalid operation")
            continue

        user_input=input("Enter the numbers separated by space (e.g 10 5 2): ").strip()
        try:
            numbers = [float(value) for value in user_input.split()]
            if not numbers:
                print("You must enter a number")
                continue
        except ValueError:
            print("You must enter a number")
            continue

        #Performing calculation
        if operation == "+":
            result = add(*numbers)
        elif operation == "-":
            result = subtract(*numbers)
        elif operation == "*":
            result = multiply(*numbers)
        elif operation == "/":#else:
            result = divide(*numbers)

        # Display result
        print(f"The result is: {result}")

        #Save to our history
        history.append(result)

if __name__ == "__main__":
    main()

