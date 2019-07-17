#This is the command line version. For more info, refer this blog post -

import sys
import requests

OpenWeatherMap_KEY = "4f04438360a1b059c0c8aa370cb983aa"

cityName = sys.argv[1]  # takes command line arguements

print("Fetching weather details for", cityName)

response = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&APPID=" + OpenWeatherMap_KEY + "&units=metric")  # API Call

res = response.json()  # Parse response to JSON

print("--------------------------------")

try:
    temp_min = str(res["main"]["temp_min"])
    temp_max = str(res["main"]["temp_max"])
    print("Requested Weather info - ")
    print("\nMinimum temperature : " + temp_min + "°C")
    print("Maximum temperature : " + temp_max + "°C")
    print("Summary - ", res["weather"][0]["description"])  # Extracting desired data from the received JSON Object

except KeyError:
    print("There were problems fetching the data. Please see below for details")
    print("Error Code -", res["cod"])
    print("Description -", res["message"])

except:
    print("An error occurred, Please see below for details")
    for item in res:
        print(item, " - ", res[item])
