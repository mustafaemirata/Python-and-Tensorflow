benimListem=[10,20,30,40,50]

print("Döngü Başladı.")
for numara in benimListem:
    print(numara*5/3)
print("Döngü bitti.")

#for num in benimListem:
#   yeniNumara=num * 5/3
#  print(yeniNumara)

yeniListe=[1,2,3,4,5,6]

for rakam in yeniListe:
    if rakam%2==0:
        print("a")
    print(rakam)

yeniString="Mustafa Emir Ata"

#for harf in yeniString:
#   print(harf)
##Tuple ile Kullanım
benimTuple=(1,2,3,4,5)

for eleman in benimTuple:
    print(eleman-10)

koordinatListesi=[(10.2,15.2),(32.4,16.2),(40.2,20.2)]
print(type(koordinatListesi[0]))

for eleman in koordinatListesi:
    print(eleman[0]) #  10.2, 32.4, 40.3 yi yazdırır

for(x,y)in koordinatListesi:
    print(y) #y değerlerini yazdırır sadece.

benimGaripListem=[(1,2,3,),(4,5,6),(7,8,9)]

for(x,y,z)in benimGaripListem:
    print(z) #Hepsinin sonar rakamlarını yazdırır.

benimSozluk={"muz":150, "portakal":250,"elma":400}
#Ayrı ayrı listelere koyma işlemi

print(benimSozluk.items())
print(type(benimSozluk.items()))

#For dögüsüyle teker teker yazdırma
for (anahtar,deger)in benimSozluk.items():
    print("Anahtar: "+anahtar)