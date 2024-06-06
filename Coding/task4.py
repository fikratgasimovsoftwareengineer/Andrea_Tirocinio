class Dog:
    def __init__(self, name, age, breed):
        self.name = name        # Public attribute
        self._age = age         # Protected attribute due to underscore
        self.breed = breed      # Public attribute

    # Property to get the age
    @property
    def age(self):
        return self._age

    # Setter for the age property with a check
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    
    # Method to provide a string representation of the dog
    def __str__(self):
        return f"{self.name} is a {self._age}-years-old {self.breed}."

# Creating an instance of the Dog class
my_dog = Dog("Jo", 3, "Siberian Husky")

# Accessing the age using the property
print(my_dog.age)  # Output: 3

# Setting the age using the property
my_dog.age = 4
print(my_dog.age)  # Output: 4

# Trying to set a negative age (will raise a ValueError)
try:
    my_dog.age = -1
except ValueError as e:
    print(e)  # Output: Age cannot be negative

# Accessing other attributes and methods
print(my_dog.name)           # Output: Jo
print(my_dog.breed)          # Output: Siberian Husky
print(my_dog)                # Output: Jo is a 4 years old Siberian Husky.
