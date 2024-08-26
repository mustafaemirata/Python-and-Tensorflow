##
class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori


    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir. : {self.kalori}"

    def __len__(self):
        return self.kalori




muz=Meyve("Muz",345)
print(muz.isim)
print(muz)
print(len(muz))
benimListem=[1,2,3,"a",4.5]
print(benimListem)

print("-----------")

elma=Meyve("Elma",200)
print(elma)
