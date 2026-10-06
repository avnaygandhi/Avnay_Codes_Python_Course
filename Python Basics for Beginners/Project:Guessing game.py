password="Avnay Codes"
hash_password=hash(password)
password_input=hash(input("Enter a guess for the password: "))
while hash_password != password_input:
    password_input=hash(input("Enter a guess for the password: "))
print("Thank you for playing. You have won")
