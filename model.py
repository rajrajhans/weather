class WeatherData:
    def __init__(self, date, max_temp, min_temp, summary, raining_chance, icon):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.summary = summary
        self.raining_prob = raining_chance
        self.icon = icon
