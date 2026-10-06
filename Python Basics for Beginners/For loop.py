# For Loop: Executes a code block a specific number of times.
# Works on any iterable object (e.g., range, string, list, dictionary).
#for count in range(5,0,-1):
    #print(f"Current count: {count}")

#name="Avnay codes"
#for number in range(len(name)):
    #print(f"Current number: {number}")
#for letter in name:
    #print(f"Current letter: {letter}")
#1.
scores=[10,20,30,40,50]
total=sum(scores)
print(total)

#2.
total=0
for score in scores:
    total=total+score
print(total)

#3.
total=0
for score in scores:
    total+=score
print(total)