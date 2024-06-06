class Dog:
    # Constructor
    def __init__(self, name, age, breed):
        self.name = name      # instance attribute
        self.age = age        # instance attribute
        self.breed = breed    # instance attribute

class Swimming:
        def swim(self):
            return "I can swim"

class Walking:
         def walk(self):
            return "I can walk"
    
class GermanShepherd(Dog, Swimming, Walking):
        def __init__(self, name, age, breed):
            self.breed = breed 
            super().__init__(name, age, breed = "German Shepherd")

        def movements(self):
                return f" Name is {self.name} and says: {self.swim()} and {self.walk()}"

# Creating an instance of GermanShepherd
gs = GermanShepherd("Ken", 5, breed= "German Shepherd")

# Accessing the methods
print(gs.movements())  
