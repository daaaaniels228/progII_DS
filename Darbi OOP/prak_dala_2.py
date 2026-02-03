class Telefons:
    def __init__(self):
        self.marka = input("Ievadiet telefona marku - ")
        self.modelis = input("Ievadiet modeli - ")
        self.krasa = input("Ievadiet krāsu - ")
        self.stavoklis = False

    def ieslegtTelefons(self):
        self.stavoklis = True

    def izslegtTelefons(self):
        self.stavoklis = False

    def zvanit(self):
        if self.stavoklis == True:
            print("Zvana...")
        else:
            print("Telefons ir izslēgts!")

    def izvadeInformacija(self):
        print(f"Telefona marka - {self.marka} \nTelefona modelis - {self.modelis} \nTelefona krāsa - {self.krasa}\n Telefons ir ieslēgts - {self.stavoklis}")

t1 = Telefons()

while True:
    
    izvele = int(input("1--ieslegt telefonu, 2 -- izslegt telefonu , 3 -- zvanit, 4 -- telefona informācija"))

    if izvele == 1:
        t1.ieslegtTelefons()
        continue
    
    elif izvele == 2:
        t1.izslegtTelefons()
        continue

    elif izvele == 3:
        t1.zvanit()
        continue
    
    elif izvele == 4:
        t1.izvadeInformacija()
        continue

    else:
        continue