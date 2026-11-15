#Linear search:A simple search algorithm that checks every element in a list sequentially until the target value is found or the list ends.
#Module:A function collection made by another programmer to make it easy for us to code

import random #Module
data=[random.randint(1,100) for i in range(20)]
print(data)

try:
    SearchValue=int(input("Enter the number you want to search for: "))
except ValueError:
    print("Sorry, this is not a number")

found=False
for index in range(len(data)):
    if data[index] == SearchValue:
        print(f"{SearchValue} was found at {index}")
        found=True

if not found:
    print("Sorry, this is not found in the list")