class Dog:
   

    def __init__(self, name, age, breed):
        self.__name = name      # Private attribute due to double underscore
        self.age = age          # Public attribute
        self.breed = breed      # Public attribute

        

    # Getter method for the private name attribute
    def get_name(self):
        return self.__name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    
    def __str__(self):
        return f"{self.get_name()} is a {self.age}-years-old {self.breed}."

# Creating instances of the Dog class
dog1 = Dog("Alex", 7, "Groenlandese")
dog2 = Dog("Ruben", 2, "Laika")

# Accessing the private name attribute using the getter method
print(dog1.get_name())  # Output: Alex
print(dog2.get_name())  # Output: Ruben

# Accessing other attributes and methods
print(dog1.age)         # Output: 7
print(dog1.breed)       # Output: Groenlandese

print(dog2.age)         # Output: 2
print(dog2.breed)       # Output: Laika

# Printing the string representation of the dogs
print(dog1)  # Output: Alex is a 7-years-old Groenlandese.
print(dog2)  # Output: Ruben is a 2-years-old Laika
