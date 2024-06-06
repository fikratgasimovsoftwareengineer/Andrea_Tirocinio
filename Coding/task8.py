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

    @staticmethod
    def number_of_paws():
        return 4

    def __str__(self):
        return f"{self.get_name()} is a {self.age}-years-old {self.breed}."

# Creating instances of the Dog class
dog1 = Dog("Jet", 3, "San Bernardo")
dog2 = Dog("Ken", 5, "Alaskan Malamute")

# Accessing the private name attribute using the getter method
print(dog1.get_name())  # Output: Jet
print(dog2.get_name())  # Output: Ken

# Accessing other attributes and methods
print(dog1.age)         # Output: 3
print(dog1.breed)       # Output: San Bernardo

print(dog2.age)         # Output: 5
print(dog2.breed)       # Output: Alaskan Malamute

# Using the static method to get the number of paws
print(Dog.number_of_paws())  # Output: 4

# Printing the string representation of the dogs
print(dog1)  # Output: Jet is a 3-years-old San Bernardo.
print(dog2)  # Output: Ken is a 5-years-old Alaskan Malamute.
