#ınstance & attrıbute
superKahramanAdi="superman"
superKahramanYasi=30
superKahramanMeslegi="Gazeteci"

ikinciSuperKahramanAdi="Batman"

class SuperKahraman:
    ozelGuc="Görünmezlik"
    def __init__(self,isimInput,yasInput,meslekInput): #Oluşturulan objenin kendisine referans veriyor (self)
        print("init çağrıldı")
        self.isim=isimInput
        self.yas=yasInput
        self.meslek=meslekInput
    def ornekMethod(self):
        print(f"ben süper kahramanım ve mesleğim {self.meslek} ")# self olmak zorunda.

# Örnek oluşturma
superman = SuperKahraman("Emir", 18, "Yazılım Mühendisi")
superman.isim=("Mahmut")
print(superman.isim)

superman.ozelGuc
superman.ornekMethod()

class Kopek():
    yilCarpani=7
    def __init__(self, yas=5):
        self.yas=yas
        self.insanYasinaCevrilmisAttribute=yas*7


    def insanYasiniHesapla(self):
        return self.yas*Kopek.yilCarpani



# Eğer değer verilmezse kayıtlı 5'i alır. Eğer değer verildiyse üzerine yazar.
benimKoepk=Kopek(10)
print(benimKoepk.yas)
print(benimKoepk.insanYasiniHesapla())

print(benimKoepk.insanYasinaCevrilmisAttribute)

