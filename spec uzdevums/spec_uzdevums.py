import requests
import json
import sqlite3

response = requests.get("https://restcountries.com/v3.1/subregion/Northern%20Europe")
print(response.status_code)

responseText = response.text
responseParsed = json.loads(responseText)

con = sqlite3.connect("Valstis")

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Valstis(
ValstisID integer NOT NULL PRIMARY KEY,
ValstsNosaukums varchar(255),
Population integer)""")

for country in responseParsed:
    teksts= str(country["name"]["common"])
    populacija = country["population"]
    print(teksts)
    cur.execute('''INSERT INTO Valstis(ValstsNosaukums,Population) VALUES(?,?)''',(teksts,populacija))

saraksts = cur.execute("SELECT ValstsNosaukums FROM Valstis").fetchall()
print(saraksts)
con.commit()
con.close()




