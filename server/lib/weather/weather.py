import requests


class WeatherAPI:
    @classmethod
    def get_data(cls):
        res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Machida,jp&appid=44db6a862fba0b067b1930da0d769e98")
        if res.status_code == 200:
            api_data = res.json()
            return Weather(api_data["name"], api_data["main"]["temp"], api_data["main"]["humidity"], api_data["weather"][0]['main'])
        else:
            None


class Weather:
    @staticmethod
    def k2c(c):
        return int(c - 273)

    def __init__(self, city, temp, humidity, state):
        self._city = city
        self._temp = Weather.k2c(temp)
        self._humidity = humidity
        self._state = state

    @property
    def temp(self):
        return self._temp

    @property
    def humidity(self):
        return self._humidity

    @property
    def state(self):
        return self._state

    def to_dict(self):
        return {"label": "outdoor", "city": self._city, "temp": self._temp, "humidity": self._humidity, "state": self._state}