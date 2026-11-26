#Classes:A blueprint or template for creating objects, defining their attributes and methods.
#Object:A specific instance of a class.
#Scope:where a variable can be seen and accessed within your code.
#Local scope:A variable created inside a function or method exists only inside that function.
#Global scope:A variable created in the main body of the script (outside all functions/classes). It can be read anywhere in the file.
#Instance Scope (self.variable in OOP): A variable attached to an object using self and lives inside the specific object instance


class car:
    def __init__(self, brand, model, year=2026):
        self.brand = brand
        self.model = model
        self.year = year
car1=car("BMW","M5")
print(car1.brand)
print(car1.model)
print(car1.year)