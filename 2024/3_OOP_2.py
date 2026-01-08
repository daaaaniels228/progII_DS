from abc import ABC 
class Skolotajs(ABC):
    stunduSk = 0
    tips = 0
    uzvards= ""

class SakumskolasSkolotajs(Skolotajs):
    
    uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu:")
    tips = 1
    klase = input("Ievadiet skolotaja klasi:")
    stunduSk = int(input("Ievadiet skolotāja stundu skaitu:"))

    def izvade(self):
        print(f"Sākumsskolas (tips-{self.tips}) skolotājs {self.uzvards} māca {self.stunduSk} {self.klase} klasē")

class VidusskolasSkoltoajs(Skolotajs):

    uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu:")
    tips = 3
    pr1 = input("Ievadiet primo pasniegto priekšmetu:")
    pr1Sk = int(input("Īevadiet pirmā priekšmeta stundu skaitu:"))
    pr2 = input("Ievadiet otro pasniegto priekšmetu:")
    pr2Sk= int(input("Ievadiet otrā priekšmeta stundu skaitu:"))

    def kopStundas(self):
        self.stunduSk = self.pr1Sk + self.pr2Sk 

    def izvade(self):
        print(f"Vidusskolas (tips-{self.tips}) skolotājs {self.uzvards} māca šadus priekšmetus: {self.pr1} un {self.pr2}, kopā {self.stunduSk} stundas")


#i1 = input("Ievadiet sākumskolas skolotāja uzvārdu:")
#i2= input("Īevadie skolotaja klasi:")
#i3 = int(input("Ievadiet skolotāja stundu skaitu"))
#i4= input("Ievadiet vidusskolas skolotāja uzvārdu")
#i5= input("Ievadiet primo pasniegto priekšmetu")
#i6= int(input("Īevadiet pirmā priekšmeta stundu skaitu"))
#i7= input("Ievadiet otro pasniegto priekšmetu")
#i8= int(input("Ievadiet otrā priekšmeta stundu skaitu"))

s1 = SakumskolasSkolotajs()
s2 = VidusskolasSkoltoajs()
s1.izvade()
s2.kopStundas()
s2.izvade()