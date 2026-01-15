import requests
import json

response=requests.get("https://restcountries.com/v3.1/all?fields=name,flags,population,area")
print(response.status_code)

if response.status_code == 200:
    print("Serveris atbild")

responseText = response.text
responseParsed =json.loads(responseText)

areaSum = 0
popSum = 0
popMax = -1
popMaxName =""
for country in responseParsed:
    popSum += country["population"]
    areaSum += country["area"]
    if (popMax<country["population"]):
        popMax = country["population"]
        popMaxName = country["name"]["common"]
    print(country["name"]["common"])

responseLatvia = requests.get("https://restcountries.com/v3.1/name/latvia?fields=borders,subregion")
responseLatviaText = responseLatvia.text
responseLvParsed = json.loads(responseLatviaText)

print(f"Latvijas subregions ir - {responseLvParsed[0]["subregion"]} un tā robežojas {responseLvParsed[0]["borders"]}")

print(f"Kopējais valstu skaits ir {len(responseParsed)} populacija {popSum/len(responseParsed)}")
print(popMax,popMaxName)
print(areaSum)







