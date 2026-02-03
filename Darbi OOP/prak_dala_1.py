class Kvadrats:
    
    def __init__(self):
        self.mala = int(input("Ievadiet malas garumu"))

    def aprekinat(self):
        laukums = self.mala * self.mala
        return laukums
    
    def izvade(self):
        print(f"Laukums ir {self.aprekinat()}")

k1 = Kvadrats()
k1.izvade()
