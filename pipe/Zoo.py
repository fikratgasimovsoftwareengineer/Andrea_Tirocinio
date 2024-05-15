
# Classe padre con costruttore

class Animal:
    def __init__(self,name,diet):
        self.name = name
        self.diet = diet

    def eat(self,diet):
        print(f"{self.name} is eating {diet}.")

# Classe dove vengono definiti i due comportamenti degli animali

class Behaviour:
    def behaviours(self,fly,swim):
        self.fly = fly
        self.swim = swim

# Classi figlie che ereditano da classe padre Animal

class Eagle(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Penguin(Animal):
    def swim(self):
        print(f"{self.name} is swimming.")
        print(f"{self.name} is flying.")

Eagle = Animal
Eagle.fly() 
Penguin = Animal
Penguin.swim()
Penguin.fly() 

# classi esempio animali e loro comportamento

class Bird(Animal):
    def behaviours(self):
        self.fly()

    def fly(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def behaviours(self):
        self.swim()

    def swim(self):
        print(f"{self.name} is swimming.")


def simulate_feeding(animal, diet):
    animal.eat(diet)


def simulate_movement(animal):
    animal.move()


if __name__ == "__main__":
    
    eagle = Bird("Eagle")
    salmon = Fish("Salmon")

    
    simulate_feeding(eagle, "insects")
    simulate_movement(eagle)

    simulate_feeding(salmon, "plankton")
    simulate_movement(salmon)
    




