class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

    # Method to provide a string representation of the dog
    def __str__(self):
        return f"{self.name} is a {self.age}-years-old dog"

# Creating an instance of the Dog class
my_dog = Dog("Jo", 3)

# Accessing attributes and methods
print(my_dog.name)           # Output: Jo
print(my_dog.age)            # Output: 3
print(my_dog)                # Output: Jo, 3
