from model import WeatherData
import requests
from geopy.geocoders import Nominatim
import time
import os

DARKSKY_SECRET_KEY = os.environ["DARKSKY_API_KEY"]  # Your DarkSky API key here

option_list = "exclude=currently,minutely,hourly,alerts&units=si"  # Asking the API to not send above data fields as we only need the "daily" datapoints


class Controller:
    def getGeocode(self, name, recursion=0):
        """Converts Location Name to Geocode using Nominatim()"""
        try:
            print("making a request to nominatim")
            geocode = Nominatim(timeout=15).geocode(name, language='en_US')
            return geocode
        except:  # To handle Nominatim timeout errors.
            if recursion > 2:
                raise KeyError
            print("making a request to nominatim again")
            time.sleep(1)
            return Controller.getGeocode(self, name)

    def getWeatherData(self, location, city):
        """This function does 4 things:\n
            1. Hit the API with a customized request and then store it in response.json
            2. Parse the response.json and extract necessary values from it (temperature - max, min, summary, raining probability, icon)
            3. Store this parsed info in a object of class model.WeatherData
            4. Return WeatherData object
        """
        current_date = ""
        max_temp = ""
        min_temp = ""
        avg_temp = ""
        summary = ""
        raining_prob = ""
        icon = ""
        errors = None
        try:
            lat = str(location.latitude)
            long = str(location.longitude)

            response_raw = requests.get(
                "https://api.darksky.net/forecast/" + DARKSKY_SECRET_KEY + "/" + lat + "," + long + "?" + option_list)
            print("https://api.darksky.net/forecast/" + DARKSKY_SECRET_KEY + "/" + lat + "," + long + "?" + option_list)
            # """Provision for including date""" response_raw = requests.get("https://api.darksky.net/forecast/" + DARKSKY_SECRET_KEY + "/" + lat + "," + long + "," + date + "?" + option_list)
            response = response_raw.json()

            current_date_epoch = response["daily"]["data"][0]["time"]
            current_date = str(time.strftime('%d-%m-%Y', time.localtime(current_date_epoch)))
            max_temp = response["daily"]["data"][0]["apparentTemperatureMax"]
            min_temp = response["daily"]["data"][0]["apparentTemperatureMin"]
            avg_temp = int((max_temp + min_temp)/2)
            summary = response["daily"]["data"][0]["summary"]
            raining_prob = "Chance of rain: %.2f%%" % (response["daily"]["data"][0]["precipProbability"] * 100)
            icon = response["daily"]["data"][0]["icon"]

        except:
            errors = "Something went wrong. Please check your city name and try again later. "
        report = WeatherData(current_date, max_temp, min_temp, avg_temp, summary, raining_prob, icon, errors, city)

        return report
