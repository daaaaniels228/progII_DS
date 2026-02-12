# class Dzinejs():

#     def iedarbina(self):
#         print("KLEKLEKLEKLEKLEKLE")

#     def izdarbina(self):
#         print("Noslāpēts")

# kleklekle = Dzinejs()
# kleklekle.iedarbina()
# kleklekle.izdarbina()

# class Auto:
#     def __init__(self):
#         self.n52 = Dzinejs()

#     def iedarbinatAuto(self):
#         self.n52.iedarbina()

#     def izsledzAuto(self):
#         self.n52.izdarbina()

# e90=Auto()
# e90.izsledzAuto()
# e90.iedarbinatAuto()

# class Gramata:

#     def __init__(self,autors,nosaukums,zanrs):
#         self.autors = autors
#         self.nosaukums = nosaukums
#         self.zanrs = zanrs


# class Biblioteka():

#     def __init__(self):
        
#         self.gramata1 = Gramata("J.K Rowling","Harijs Poters Un Five Lakes Noslēpums","romāns")
#         self.gramata2 = Gramata("Svens Kuzmins","Brīvībene","Proza")
#         self.gramSaraksts = [self.gramata1,self.gramata2]

#     def apskatitGramatas(self):
#         for gramata in self.gramSaraksts:
#             print(gramata.autors,gramata.nosaukums,gramata.zanrs)

        

#     def mekletGramatu(self):
#         meklejums = input("Ievadi grāmatas nosaukumu")
#         for gramata in self.gramSaraksts:
#             nosaukums = gramata.nosaukums
#             #print(nosaukums.find(meklejums))

#             if nosaukums.find(meklejums) != -1:
#                 print(nosaukums)
#             else:
#                 print("neatrada")

    
# skolasBiblioteka = Biblioteka()
# skolasBiblioteka.apskatitGramatas()
# skolasBiblioteka.mekletGramatu()

class Ram():
    def __init__(self,info,stavoklis):
        self.info = info
        self.stavoklis = stavoklis

    def izvaditInfo(self):
        print("Ram",self.info,self.stavoklis)

    def ieslegt(self):
        self.stavoklis = "Ieslegts"

    def izslegt(self):
        self.stavoklis = "Izslegts"

class Cpu():
    def __init__(self,info,stavoklis):
        self.info = info
        self.stavoklis = stavoklis

    def izvaditInfo(self):
        print("Cpu",self.info,self.stavoklis)

    def ieslegt(self):
        self.stavoklis = "Ieslegts"

    def izslegt(self):
        self.stavoklis = "Izslegts"

class Psu():
    def __init__(self,info,stavoklis):
        self.info = info
        self.stavoklis = stavoklis

    def izvaditInfo(self):
        print("Psu",self.info,self.stavoklis)

    def ieslegt(self):
        self.stavoklis = "Ieslegts"

    def izslegt(self):
        self.stavoklis = "Izslegts"

class Gpu():
    def __init__(self,info,stavoklis):
        self.info = info
        self.stavoklis = stavoklis

    def izvaditInfo(self):
        print("Gpu:",self.info,self.stavoklis)

    def ieslegt(self):
        self.stavoklis = "Ieslegts"

    def izslegt(self):
        self.stavoklis = "Izslegts"

        


class Dators():

    def __init__(self):
        self.ram = Ram("HyperX DDR5 5600MHz 32GB","Ieslegts")
        self.cpu = Cpu("Intel 12900K 3.2GHz", "Izslegts")
        self.psu = Psu("Akyga basic 420W", "Izslegts")
        self.gpu = Gpu("Nvidia GeForce 5090 32GB","Izslegts")
        self.kompenetes = [self.ram,self.cpu,self.psu,self.gpu]

    def ieslegt(self):

        for komp in self.kompenetes:
            komp.ieslegt()
            #print(komp.stavoklis)

    def izslegt(self):
        for komp in self.kompenetes:
            komp.izslegt()
            #print(komp.stavoklis)

    def apskatit(self):

        for komp in self.kompenetes:
            komp.izvaditInfo()

kreditDators = Dators()
kreditDators.ieslegt()
kreditDators.izslegt()
kreditDators.apskatit()


