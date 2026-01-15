class csdd:

    def __init__(self):
        self.zimols = input("Ievadi zīmolu - ")
        self.modelis = input("Ievadi modeli - ")
        self.datums = str(f"{int(input("Ievadi reģistrācijas dienu - "))}.{int(input("Ievadi reģistrācijas mēnesi - "))}.{int(input("Ievadi reģistrācijas gadu - "))}")
        self.masa = int(input("Ievadi transportlīdzekļa pilno masu - "))
        self.veids = input("Ievadi transport līdzekļa degvielas viedu (iespējamie apzīmējumi: B-benzīns ,BG – benzīns/gāze, D – dīzeļdegviela,E – elektriskais, BE – benzīna hibrīds, DE – dīzeļa hibrīds) -  ")


    def izvade(self):
        print(f"zīmols: {self.zimols}")
        print(f"modelis: {self.modelis}")
        print(f"reģistrācijas datums: {self.datums}")
        print(f"pilna masa: {self.masa}")
        print(f"degvielas veids: {self.veids}")        
car1 = csdd()
car1.izvade()