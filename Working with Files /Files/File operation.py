#File handing:The process of reading data from and writing data to files stored on a computer's disk using a program
#Used to score data such as high score in a game

#1.
with open('file.txt', 'w') as file:
    file.write("Welcome to Avnay Codes channel\n")

#2.
file=open('file.txt', 'w')
file.write("Welcome to Avnay Codes channel\n")
file.close()

#Appeding('a')
with open('file.txt', 'a') as file:
    file.write("Welcome to Python file handling video \n")


#Read
with open('file.txt', 'r') as file:
    print(file.read())

try:
    with open('file.txt', 'r') as file:
        text=file.read()
        print(text)
except FileNotFoundError:
    print('File not found')

#String manipulation
print(text[0:5])#Last index-starting index=Character length
print(text[0:-5])