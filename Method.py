#Classes:A blueprint or template for creating objects, defining their attributes and methods.
#Object:A specific instance of a class. It is a concrete entity created from the class blueprint and has its own state (values for its attributes).
#Scope:where a variable can be seen and accessed within your code.
#Local scope:A variable created inside a function or method exists only inside that function. Once the function finishes running, the variable is destroyed.
#Global scope:A variable created in the main body of the script (outside all functions/classes). It can be read anywhere in the file.
#Instance Scope:A variable attached to an object using self. It lives inside the specific object instance and can be accessed by any method inside that class using self.
#Method:A procedure or function defined within a class that defines the actions or behaviors an object can perform.
#Attribute:A piece of data stored within a class or object that defines its state or properties.
#Setter:A public method used to safely update or set the value of a private attribute.
#Getter:A public method used to safely retrieve the value of a private attribute.

class car:
    def __init__(self, brand, model, year=2026):
        self.__brand = brand#Private
        self.__model = model
        self.__year = year
    def display(self):
        print(f"The car brand is {self.__brand}, car model is {self.__model}, it was made in {self.__year}")
    def GetBrand(self):
        return self.__brand
    def GetModel(self):
        return self.__model
    def GetYear(self):
        return self.__year
    def SetYear(self, year):
        self.__year = year
car1=car("BMW","M5",2013)
car1.display()
car1.SetYear(2020)
car1.display()
print(car1.GetBrand())
