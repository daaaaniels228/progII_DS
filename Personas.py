from abc import ABC, abstractmethod

class Persona(ABC):
    
    def __init__(self,vards,uzvards):
        self.vards = vards
        self.uzvards = uzvards
    @abstractmethod
    def sitiesPrieksa():
        pass


class Skolens(Persona):

    def __init__(self,vards,uzvards,klase):
        super().__init__(vards,uzvards)
        self.klase = klase

    def staditiesPrieksa(self):
        return(print(f"{self.vards},{self.uzvards},{self.klase}"))
    
class Skolotajs(Persona):
    
    def __init__(self, vards, uzvards,prieksmeti):
        super().__init__(vards, uzvards)
        self.prieksmeti = prieksmeti

    def staditiesPrieksa(self):
        return(print(f"{self.vards},{self.uzvards},{self.prieksmeti}"))

    
s1 = Skolens("Janis","Berzins","12.id")

#s1.staditiesPrieksa()
saraksts = ["Matematika","Fizika"]
p1 = Skolotajs("Harijs","Potters",saraksts)
#p1 = Skolotajs("Harijs","Potters",["Matematika","Fizika"])
saraksts[1] = "Ģeogrāfija"
p2 = Skolotajs("Simona","Lodziņa",saraksts)
#p1.staditiesPrieksa()
#p2.staditiesPrieksa()
rinda=[p1,s1]
for i in rinda:
    i.staditiesPrieksa()
#rinda.staditiesPrieksa(self)
