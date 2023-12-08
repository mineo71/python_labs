import csv

class WeatherData:
    def __init__(self, date, temperature, humidity, pressure):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def __str__(self):
        return f"{self.date}: температура {self.temperature}, вологість {self.humidity}, тиск {self.pressure}"


class Temperature(WeatherData):
    def average_temperature(self, data):
        total_temperature = sum(weather_data.temperature for weather_data in data)
        return total_temperature / len(data) if len(data) > 0 else 0


class Humidity(WeatherData):
    def highest_humidity(self, data):
        return max(weather_data.humidity for weather_data in data) if len(data) > 0 else 0


class Pressure(WeatherData):
    def lowest_pressure(self, data):
        return min(weather_data.pressure for weather_data in data) if len(data) > 0 else 0


def main():
    try:
        with open("extra_tasks/weather.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            data = []
            for row in reader:
                if len(row) == 4:
                    date = row[0]
                    temperature = float(row[1])
                    humidity = float(row[2])
                    pressure = float(row[3])
                    data.append(WeatherData(date, temperature, humidity, pressure))

        temperature_data = Temperature("", 0, 0, 0)
        humidity_data = Humidity("", 0, 0, 0)
        pressure_data = Pressure("", 0, 0, 0)

        print("Середня температура:", temperature_data.average_temperature(data))
        print("Найвища вологість:", humidity_data.highest_humidity(data))
        print("Найменший тиск:", pressure_data.lowest_pressure(data))
    except FileNotFoundError:
        print("Файл weather.csv не знайдено.")
    except ValueError:
        print("Файл weather.csv має некоректний формат.")


if __name__ == "__main__":
    main()
