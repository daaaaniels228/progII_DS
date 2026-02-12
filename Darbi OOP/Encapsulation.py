class Skolens:

    def __init__(self,atzime,vards):
        self.__atzime = atzime
        self.__vards = vards

    @property
    def atzime(self):
        if 1<= self.__atzime >= 10:
            print("Nepareiza atzime")
        else:
            pass
    @property
    def vards(self):
        if type(self.__vards) != str:
            print("neeee")
        else:
            pass 

    
audzeknis1= Skolens(12,2)
print(audzeknis1)