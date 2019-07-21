from flask import Flask, request, render_template
from controller import Controller

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/weather', methods=["GET", "POST"])
def weather():
    weatherObj = None
    errors_geo = None
    if request.method == "POST": #Handling the form request
        city = request.form["city"]
        wr = Controller()
        try: #Error will come if city name is wrong or there is a problem with DarkSky servers.
            location = wr.getGeocode(city)
            weatherObj = wr.getWeatherData(location, city)
        except:
            errors_geo = "Something went wrong. Please check your city name and try again later. "
    return render_template("weather.html", weather=weatherObj, errors_geo=errors_geo) #sending the weatherObj object which contains all the required data to render.


if __name__ == '__main__':
    app.debug=True
    app.run()
