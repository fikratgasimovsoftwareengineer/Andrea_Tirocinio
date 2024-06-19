class Zoo:
    def __init__(self, animal, breed, health):
        self.animal = animal
        self.breed = breed
        self.health = health

    def add_animals(self, new_animal):
        
        self.new_animal = new_animal
        return new_animal

    def feed_animals(self, animal_name):
        self.animal_name = animal_name
        return animal_name
    
    def track_health(self, health):
        self.health = health
        return health




class Mammal(Zoo):

    def __init__(self, animal, breed, track_health):
        super().__init__(animal, breed, track_health)

        
    

class Bird(Zoo):

    def __init__(self, animal, breed,track_health):
        super().__init__(animal, breed, track_health)
        


class Reptile(Zoo):

    def __init__(self, animal, breed, track_health):
        super().__init__(animal, breed, track_health)
        



def main():
    animal = "dog"
    feedname = "dogood"
    goodhealth  = "health"
    mamal = Mammal(animal,feedname,goodhealth)
    print(mamal.add_animals(animal))
    print(mamal.feed_animals(feedname))
    print(mamal.track_health(goodhealth))

    animal2 = "eagle"
    feedname2 = "eaglegood"
    goodhealth2 = "health2"
    bird = Bird(animal2, feedname2, goodhealth2)
    print(bird.add_animals(animal2))
    print(bird.feed_animals(feedname2))
    print(bird.track_health(goodhealth2))

    animal3 = "python"
    feedname3 = " pythongood"
    goodhealth3 = "health3"
    reptile = Reptile(animal3,feedname3,goodhealth3)
    print(reptile.add_animals(animal3))
    print(reptile.feed_animals(feedname3))
    print(reptile.track_health(goodhealth3))

if __name__ == "__main__":
    main()
 