class kubs:

    def __init__(self,mGarums,krasa):
        self.mGarums = int(mGarums)
        self.krasa = krasa
        try:
            if 2<= self.mGarums <=10:
                print(self.mGarums)#self.mGarums = mGarums
            else:
                print("neatbilst intervālam")

        except:
            print("ex")
            
            pass

    # def __init__(self):
    #     self.mGarums = 0 
    #     self.krasa = ""
    
    #     while True:
    #         try:
    #             i1 = int(input("ievadi kuba malas garumu (malas atļautais garums no 2 līdz 10 ieskaitot)"))
    #             if 2 <= i1 <= 10:
    #                 self.mGarums = i1
    #                 break
    #             else:
    #                 print("Garums neiekļaujas intervālā")
    #                 continue
    #         except:
    #             print("Notikusi kļūda")
    #             continue

    #     while True:
    #         try:
    #             i2 = str(input("Ievadi krāsas nosaukumu (viens vārds) - "))
    #             if len(i2.split()) == 1 and i2.isalpha() == True:
    #                 self.krasa = i2
    #                 break
    #             else:
    #                 print("Krāsa nav uzrakstīta vispār vai arī ir par 1 vārdu vairāk")
    #                 continue
                
    #         except:
    #             print("Notikusi kļūda")
    #             break

kubg=kubs(2,"eqw")