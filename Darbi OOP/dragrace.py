import time
import random

class Auto:

    def __init__(self,modelis,gads):
        self.modelis = modelis
        self.gads = gads
        self.atrums = 0
        self.iedarbinats = False
    
    def start(self):
        self.iedarbinats = True

    def paatrinajums(self):
            if self.iedarbinats == True:
                self.atrums += random.randint(1,5)
            #print(self.atrums)

class PretiniekaAuto(Auto):
    
    def __init__(self):
        rusasSpaini = {"Volga": 1964,
                    "Pobeda": 1943,
                    "Ņiva" : 1999,
                    "Žigulis":1974,
                    "Uaz 3303": 1986,
                    "Moskvičs":1989,
                    "Žuks":1977,
                    "Čaika":1067,
                    "Zaparožets":1991,
                    "Samāra":1990}
        
        modelis,gads = random.choice(list(rusasSpaini.items()))
        self.modelis = modelis
        self.gads = gads

    

print(f"Tikko no Padomju Savienības un bez rūsas\n"
"******************************************")

m1 = Auto(input("Ar ko brauksi (Ievadi modeli) - "),int(input("Kura gada mistakste tev ir (Ievadi gadu) - ")))
m2 = PretiniekaAuto()

print(f"Tavs Auto{m1.modelis} ({m1.gads})\n"
f"Pretinieka auto:{m2.modelis} ({m2.gads})")

uzsaktIevade = int(input("Iedarbini mašīnu ar 1"))

if uzsaktIevade == 1:
    m1.start()
    print(f"Spēlētāja {m1.modelis} ({m1.gads}) tiek iedarbināts...")
    m2.start()
    print(f"Pretinieka {m2.modelis} ({m2.gads}) tiek iedarbināts")
    print("Gatavojies!")

    for i in range(1,4):
        print(i)
        time.sleep(1)

    laiksSakuma = time.time()
    print("Dod gāzi ar Enter")

    while True:

        if m1.atrums < 100 and m2.atrums < 100:
            ievade = input("")
            if ievade == "":
                m1.paatrinajums()
                m2.paatrinajums()
                print(f"Tavs -{m1.atrums}   Pretinieka-{m2.atrums}")
                continue
        else:

            if m1.atrums > m2.atrums:
                print(f"Volga nobruka! Malacis, tu uzvarēji!")
            
            else:
                print("Rūsas klucis tevi izkoda. KAUNIES!")
            
            break
    print(f"Mašīnu braukšanas laiks:{time.time() - laiksSakuma:.2f} sekundes")
else:
    print("Atslēgas aizmirsi??? Pretinieks uzvarēja")
