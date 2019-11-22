from PyDictionary import PyDictionary
search = input("Enter a word:")
try:
    myDict = PyDictionary(search)
    print("Meanng")
    print(myDict.getMeanings())
    print("Synonym")
    print(myDict.getSynonyms())
except:
    print("Not a legal word")
    