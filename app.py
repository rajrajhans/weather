from flask import Flask, request, render_template
from controller import Controller

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/weather', methods=["GET", "POST"])
def weather():
    weatherObj = None
    if request.method == "POST":
        city = request.form["city"]
        wr = Controller()
        location = wr.getGeocode(city)
        weatherObj = wr.getWeatherData(location)
    return render_template("weather.html", weather=weatherObj)


if __name__ == '__main__':
    app.debug=True
    app.run()
