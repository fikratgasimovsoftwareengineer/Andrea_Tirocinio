class Observer:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError("Subclass must implement abstract method")

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_weather_data(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

    def get_weather_data(self):
        return {
            "temperature": self._temperature,
            "humidity": self._humidity,
            "pressure": self._pressure,
        }

class WeatherDisplay(Observer):
    def __init__(self, name):
        self.name = name
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print(f"{self.name} - Temperature: {self._temperature}°C, Humidity: {self._humidity}%, Pressure: {self._pressure} hPa")

def main():
    weather_station = WeatherStation()

    display1 = WeatherDisplay("Display 1")
    display2 = WeatherDisplay("Display 2")

    weather_station.register_observer(display1)
    weather_station.register_observer(display2)

    weather_station.set_weather_data(25, 65, 1013)
    weather_station.set_weather_data(26, 70, 1012)

    weather_station.remove_observer(display1)
    weather_station.set_weather_data(27, 75, 1011)

if __name__ == "__main__":
    main()
