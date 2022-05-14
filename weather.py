"""import requests

r = requests.get('https://www.metaweather.com/api/location/2455920')
d = r.json()
for day in d['consolidated_weather']:
	print(f"{day['applicable_date']}\tHumidity: {day['humidity']}")"""

# TO DO:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
#
# To test your code, open a terminal below and run:
#   python3 weather.py


import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    for day in weather['consolidated_weather']:
        date = day['applicable_date']
        state = day['weather_state_name']
        maxF = round(day['max_temp'] * 9/5 + 32, 1)
        minF = round(day['min_temp'] * 9/5 + 32, 1)
        print(f"Date: {date}\t{state}\t\tMax Temp (degrees F): {maxF}\t Min Temp (degrees F): {minF}")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")


def weather_dialog():
    where = ''
    while not where:
        where = input("Where in the world are you? ")
    try:
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is.")
        elif len(locations) > 1:
            disambiguate_locations(locations)
        else:
            woeid = locations[0]['woeid']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
    	print("Connection Error!")


if __name__ == '__main__':
    while True:
        weather_dialog()