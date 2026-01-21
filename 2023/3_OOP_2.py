class kubs:

    def __init__(self,mGarums,krasa):
        self.mGarums = int(mGarums)
        self.krasa = krasa
        try:
            if 2<= self.mGarums <=10:
                print(self.mGarums)#self.mGarums = mGarums

            else:
                if self.mGarums < 2 :
                    self.mGarums = 2
                elif self.mGarums > 10:
                    self.mGarums = 10

            if len(self.krasa.split()) != 1 and self.krasa.isalpha() == True:
                print("nav krasa uzrakstīta vienā vārdā")

        except Exception as e:
            print(e)
            

    def aprekinat_tilpumu(self):
        tilpums = self.mGarums ** 3
        return tilpums
    
    def __del__(self):
        pass
 

kubg=kubs(10,"zaļa")
kubr=kubs(1,"sarkans")
print(f"{kubg.krasa,kubg.aprekinat_tilpumu()} cm3")
print(kubr.mGarums)
del kubr
try:
    print(kubr.krasa)
    print("nav izdzests")

except Exception as e :
    print(f"Izdzēsts {e}")
print(kubg.mGarums)

class bloks(kubs):

    def __init__(self,kubuSk,forma):
        # self.__kubuSk = kubuSk
        # self.nosaukums = nosaukums
        # self.forma = forma
        # self.derigums = derigums
        

        try:
            if 11>= int(forma) <=14 or int(forma) == 22:
                self.derigums = 1 
            else:
                self.derigums = 0

            if 1>=int(kubuSk) <= 4:
                self.kubuSk = kubuSk
            else:
                print("Kubu skaits neatbilst intervālam")
        except Exception as e:
            print(f"Kļūda: {e}")

        self.nosaukums = self.krasa,self.kubuSk

    def tilpums(self):
        blokTilpums = self.kubuSk * self.mGarums**3
        print(blokTilpums)


o1.bloks(5,"oranžs",3,13)


                 
