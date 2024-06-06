class Dog:
    #class variable
    species = "Canis familiaris"
    # Constructor
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

    #class variable each time a new instance is created
    
        Dog.species = "Canis familiaris"

    # Method to provide a string representation of the dog
    def __str__(self):
        return f"{self.name} is a {self.age}-years-old dog"

# Creating an instance of the Dog class
my_dog = Dog("Jo", 3)
your_dog = Dog("John", 6)

# Accessing attributes and methods
print(my_dog.name)           # Output: Jo
print(my_dog.age)            # Output: 3
print(my_dog)                # Output: Jo, 3
print(my_dog.species)        # Output: Canis familiaris
print(your_dog)              # Output: John, 6
print(your_dog.species)      # Output: Canis familiaris