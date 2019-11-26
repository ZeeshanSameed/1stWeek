import requests


APP_ID = 'd01ff7450d72d4b98014a97d3efe7dd0'
API_ADDRESS = 'http://api.openweathermap.org/data/2.5/weather?appid={}&q='.format(APP_ID)

choice = "yes"
while choice is "yes" or choice is "Yes":
    city = input("Enter city name: ")
    print('\n', '*' * 50)
    
    json_data = requests.get("{}{}".format(API_ADDRESS, city)).json()
    temprature_in_k = json_data['main']['temp']


    # TODO: Check the response code. and make the proper flow
    # TODO: make the function for conversions

    celsius = temprature_in_k - 273.15
    fahrenheit = temprature_in_k * 9/5 - 459.67

    print("Temperature in {} will be:".format(city))
    print("\tKelvin: ", temprature_in_k)
    print("\tCelsius: ", celsius)
    print("\tFahrenheit: ", fahrenheit)
    print('*' * 50)

    print("Do you want to search for another city?")
    choice = input("Type yes or no: ")
