import requests, json

c = "yes"

while c != "no":

    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d01ff7450d72d4b98014a97d3efe7dd0&q='

    city = input ("Enter City Name :")

    url = api_address + city

    json_data = requests.get(url).json()

    j_data = json_data['main']["temp"]

    print(j_data)

    print("Do you want to search for another cty name?")

    c = input ("type yes or no \n")
