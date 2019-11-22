import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
n="yes"
while n != "no":
    querystring = {"term":"wat"}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "acedef397amshdbe6c691713f8e2p13e0fcjsn2561abe96460"
        }

    querystring["term"] = input("Enter a word: \n")
    n = querystring["term"]


    response = requests.request("GET", url, headers=headers, params=querystring).json()
    definitions = response['list']
    definition = definitions[0]['definition']
    example = definitions[0]['example']
    print(definition)
    print(example)
    print("\n Do you want to search for another cty name?")
    n = input ("type yes or no \n")
