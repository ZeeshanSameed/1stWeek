import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
choice="yes"
while choice == "yes" or choice == "Yes":
    querystring = {"term":"wat"}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "acedef397amshdbe6c691713f8e2p13e0fcjsn2561abe96460"
        }

    querystring["term"] = input("Enter a word: \n")

    #if isinstance(querystring["term"], str):
    try:    
        choice = querystring["term"]


        response = requests.request("GET", url, headers=headers, params=querystring).json()
        definitions = response['list']
        definition = definitions[0]['definition']
        example = definitions[0]['example']
    
        print("Definiton is: \n",definition)
        print("Examples would be:\n",example)
        print("\n Do you want to search for another word?")
        choice = input ("type yes or no \n")
    
    except(IndexError,KeyError,ValueError,TypeError):
        print("\n Not a valid word do you want to search for another word?")
        choice = input ("type yes or no \n")
