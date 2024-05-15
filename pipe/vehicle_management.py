class Vehicle:

	def __init__ (self, make , model):
		self.make = make
		self.model = model

	def display_info(self):
		return f"vehicle : {self.make} {self.model}"

class Car(Vehicle):

	def __init__(self, make, model, car_type):

		super().__init__(make, model)

		self.car_type=car_type
		
	def display_info(self):
		return f"vehicle : {self.make} {self.model}"

if __name__ == "__main__":
	# Create instances of Car and Motorcycle
    my_car = Car("Toyota", "Corolla", "Sedan")
    print(my_car.display_info())
