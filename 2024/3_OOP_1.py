class Dokotorats:
    #def __init__(self,doktoNosaukums, doktoSk):
     #   self.doktoNosaukums = doktoNosaukums
      #  self.doktoSk = doktoSk

    def ievade(self):

        i1 = input("Ievadi doktorata nosaukumu")
        i2 = input("Ievadi pacientu skaitu")
        self.doktoNosaukums = i1
        self.doktoSk = i2

    def izvade(self):
        print(f"{self.doktoNosaukums}{self.doktoSk}")

klaseNew = Dokotorats()

klaseNew.ievade()
klaseNew.izvade()