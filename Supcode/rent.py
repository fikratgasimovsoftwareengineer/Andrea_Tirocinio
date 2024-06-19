from datetime import datetime

class Vehicle:

    def __init__(self, brand, model, year, hourly_rate):
        self.brand = brand
        self.model = model
        self.year = year
        self.hourly_rate = hourly_rate
        self.rental_start_time = None


class Car(Vehicle):

    def __init__(self, brand, model, year, hourly_rate, fourtires):
        super().__init__(brand, model, year, hourly_rate)
        self.fourtires = fourtires


class Bike(Vehicle):

    def __init__(self, brand, model, year, hourly_rate, twotires):
        super().__init__(brand, model, year, hourly_rate)
        self.twotires = twotires


class RentalService(Vehicle):

    def __init__(self, brand, model, year, insurance, hourly_rate):
        super().__init__(brand, model, year)
        self.insurance = insurance
        self.hourly_rate = hourly_rate
        self.vehicles = []

    def rental_charge(self):

        rental_duration = datetime.now() - self.rental_start_time
        rental_hours = rental_duration.total_seconds() / 3600
        total_charge = rental_hours * self.hourly_rate
    
    def vehicle_available(self):

        for vehicle in self.vehicles():
            print("Vehicles are:" + vehicle)

def main():
    brand = "Fiat"
    model = "Panda"
    year = 2023
    hrate = 45
    fourtires = "yes"
    car = Car(brand,model,year,hrate,fourtires)
    print(f"Car: {car.brand}, {car.model}, anno : {car.year}")
    print(f"Tariffa: {car.hourly_rate}, {car.fourtires}")

    brand2 = "BMW"
    model2 = "RT 800"
    year2 = 2015
    hrate2 = 40
    twotires = "yes"
    bike = Bike(brand2,model2,year2,hrate2,twotires)
    print(f"Bike : {bike.brand},{bike.model}, anno : {bike.year}")
    print(f"Tariffa : {bike.hourly_rate},{bike.twotires}")

if __name__ == "__main__":
    main()
