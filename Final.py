import json,requests
#city detection
city = input("please put in your city(first letter capital): ")
#initialising variables for the api key to get weather data
api_key = "e6b6e952968c4f6d8ba143842220605"
base_url = "http://api.weatherapi.com/v1/forecast.json?key="
#asking city and using it to generate the url to use
complete_url = base_url + api_key + "&q=" + str(city) + "&alerts=yes"
#requesting data for the city and storing it in # XXX:
response = requests.get(complete_url)
x = response.json()
#storing the main key in y
try:
    y = x["current"]
except:
    print("error: city not found")
    exit()
z = x["alerts"]
print()
print("The Current Temperature is " + str(int(y["temp_c"])) +  " Degrees Celcius")
print()
print("The Current Wind Speed is "+ str(float(y["wind_kph"])) + " Kilometers per hour")
print()
print("The Current Precipetation is " + str(float(y["precip_mm"])) + " Milimeters")
print()
alerts = z["alert"]
if alerts != []:
    alerts2 = alerts[0]
    print("WARNING:")
    print(alerts2["headline"])
    print()
else:
    pass

if y["temp_c"] > 35 or y["temp_c"] < -25:
    print("WARNING:")
    print("Extreme temperatures, Be careful")
    print()
if y["wind_kph"] > 57:
    print("WARNING:")
    print("Extreme winds, Be careful")
    print()
if y["precip_mm"] > 40:
    print("WARNING:")
    print("Lots of rain, Be careful")
