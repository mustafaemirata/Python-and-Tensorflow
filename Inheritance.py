class Hayvan:
    def __init__(self):
        print("Hayvan sınıfı init çağırıldı.")

    def metot1(self):
        print("Hayvan sınıfı metot1 çağrıldı")

    def metot2(self):
        print("Hayvan sınıfı metot2 çağrıldı")


benimHayvanim = Hayvan()
benimHayvanim.metot1()


class Kedi(Hayvan):
    def __init__(self):
        super().__init__()  # Üst sınıfın init metodunu çağır
        print("Kedi sınıfı init çağırıldı")
    def miyavla(self):
        print("miyavv")

    #Override
    def metot1(self):
        print("Kedi sınıfındaki metot1 çağrıldı")


benimKedi = Kedi()
benimKedi.miyavla()
benimKedi.metot1()

digerHayvan=Hayvan()
digerHayvan.metot1()

digerKedi=Kedi()
digerKedi.metot1()

## Polymorphism ##

class Elma():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim+" 100 kaloridir."

class Muz():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim+" 150 kaloridir."

elma=Elma("elma")
print(elma.bilgiVer())

muz=Muz("muz")
print(muz.bilgiVer())
print("--------------")
meyveListesi=[elma,muz]

for meyve in meyveListesi:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())

bilgiAl(muz)



