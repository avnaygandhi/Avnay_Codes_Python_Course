#Binary Search:An efficient search algorithm for sorted lists. It repeatedly divides the search interval in half.
#Recursion:programming technique where a function calls itself directly or indirectly to solve a subproblem.

#1.Normal
import random
data = [random.randint(0, 100) for x in range(15)]
#1a-Python function
print("1a answer")
data.sort()
print(data)
#1b-Bubble sort
print("1b answer")
number_elements = len(data)#15
swapped = True
while swapped:
    swapped = False
    for index in range(number_elements - 1):
        if data[index] > data[index + 1]:
            swapped = True
            data[index], data[index + 1] = data[index + 1], data[index]#Pythonic way
            #temp=data[index]
            #data[index]=data[index+1]
            #data[index+1]=temp
print(data)
SearchValue=int(input("Enter the number you want to search for: "))


