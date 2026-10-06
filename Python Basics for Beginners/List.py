#List:built-in data structure used to store a collection of items under a single variable name.
fruits=["Apple","Banana","Orange"]
print(fruits)

#Indexing
for index in range(len(fruits)):
    print(f"The fruit at {index} index is {fruits[index]}")
#print(fruits[1:3])

#Add an element to existing list
#fruits.append("Mango")
#print("New fruits list",fruits)

#Remove an element
#fruits.remove("Mango")
#print("New fruits list without mango",fruits)

# Change an element
fruits[1]="Coconut"
print(f"The fruit at {1} index is now {fruits[1]}")

fruits.sort()
print(fruits)
