

class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

class GermanShepherd(Dog):
    #Constructor
    def __init__(self, name, age, strength):
        super().__init__(name,age) #call the constructor of the dog class
        self.strength = strength   #new instance attribute

    # Creating an instance of GermanShepherd
german_dog = GermanShepherd("Jo", 5, "German Shepherd")

# Accessing attributes and methods from  both Dog and GermanShpherd classes
print(german_dog.name)          # Output: Jo
print(german_dog.age)           # Output: 5       
print(german_dog.strength)      # Output: German Shepherd
