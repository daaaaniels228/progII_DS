import requests
import json
import sqlite3
import os

if os.path.exists("History.db"):
    pass
else:
    with open("History.db","x"):
        con = sqlite3.connect("History.db")
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS History(
        ID INTEGER NOT NULL PRIMARY KEY,
        Country varchar(50),
        Universeties INTEGER)''')


con = sqlite3.connect("History.db")
cur = con.cursor()
while True: 
    sakumIevade = int(input("1--Pievienot jaunus datus     2--Apskatīt esošos"))

    if sakumIevade == 1:
        valstsIevade = input("Ievadiet valsti kuru meklēt").capitalize()
        cur.execute('''SELECT Universeties FROM History WHERE Country=?''',(valstsIevade,))
        res = cur.fetchone()
        print(type(res))
        print(res)
        
        if res == None : 
            response = requests.get("http://universities.hipolabs.com/search?country="+valstsIevade)
            responseText = response.text
            responseParsed = json.loads(responseText)
            uniSk = 0
            for uni in responseParsed:
                uniSk +=1
            print(valstsIevade,uniSk)
            cur.execute("INSERT INTO History (Country,Universeties) VALUES (?,?)",(valstsIevade,uniSk))
    elif sakumIevade == 2:
        cur.execute("SELECT * FROM History")
        print(cur.fetchall())
    beiguIevade = int(input("1--- Sākt no jauna     2---Beigt darbu"))

    if beiguIevade == 2:
        con.commit()
        con.close()
        break
    elif beiguIevade == 1:
        continue
        

        