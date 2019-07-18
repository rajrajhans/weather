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
    if request.method == "POST":
        city = request.form["city"]
        wr = Controller()
        try:
            location = wr.getGeocode(city)
            weatherObj = wr.getWeatherData(location)
        except:
            errors_geo = "Something went wrong. Please check your city name and try again later. "
    return render_template("weather.html", weather=weatherObj, errors_geo=errors_geo)


if __name__ == '__main__':
    app.debug=True
    app.run()
