
# Classe padre con costruttore

class Vehicle:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

# classe model

class VehicleManagementSystem:
    def __init__(self):
        self.vehicles = []

    def display_info(self, manufacturer, model, year):
       
        

#  classe figlia che eredita da vehicle
          
class Car(Vehicle):
    def __init__(self, manufacturer, model, year, is_electric=False):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.is_electric = is_electric

    def display_info(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Is Electric: {self.is_electric}")


#  classe figlia che eredita da vehicle

class Moto(Vehicle):

    def __init__(self, manufacturer, model, year, has_sidecar=False):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.has_sidecar = has_sidecar

    def display_info(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Has sidecar: {self.has_sidecar}")

# funzione di controllo principale

def main():

    management_system = VehicleManagementSystem()


    car = Vehicle("Ford","Ranger","2024", is_electric=True)
    car.display_info()

    moto = Vehicle("Cagiva","Planet","2000",has_sidecar=True)
    moto.display_info()

    vehicle = [car, moto]

    for vehicle in vehicle:
	    vehicle.display_info()

if __name__ == "__main__":
    main()
 



    
    

    
