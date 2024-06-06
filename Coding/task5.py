class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

    # Method to make the dog bark
    def speak(self):
        return f"{self.name} says Woof!"
    
class GermanShepherd(Dog):
    #Constructor
    def __init__(self, name, age):
        super().__init__(name,age) #call the constructor of the dog class

    def speak(self):
        # Overriding the bark method
        return f"{self.name} says Wooooooooof!"

#creating the instance of dog class
my_dog = Dog('Wild',4)
#creating the instance of germanshepherd class
german_dog = GermanShepherd('John',5)

#accessing attributes and methods

print(my_dog.name)
print(my_dog.age)
print(my_dog.speak())
print(german_dog.name)
print(german_dog.age)
print(german_dog.speak())
