from random import randint,shuffle

benimListem=[0,1,2,3,4,5,6]

#Range (Genişlik)

print(list(range(25)))

print(list(range(5,21,4))) # ilk elemanla başla son elemana eşitse onu yazdırma. 4'er 4'er atlayarak git.

#Enumerate

index=0

for numara in list(range(5,15)):
    print(f"güncel numara: {numara} güncel index: {index}")
    index=index+1

for eleman in enumerate(list(range(5,15))):
    print(eleman) #type'ı tuple'dır
print("----------------")
for (index,numara) in enumerate(list(range(5,15))):
    print(index,numara) # type'ı tuple'dır

print("-----------")

#RANDOM

print(randint(0,100))

yeniListe=list(range(0,10))
print(yeniListe[randint(0,9)])

# Rastgele dizi iiçinde dağılım (shuffle)

shuffle(yeniListe)
print(yeniListe)

# ZIP

yemekListesi=["muz","ananas","elma"]
kaloriListesi=[100,200,300]
gunListesi=["pazartesi","salı","çarşamba"]

zip(yemekListesi,kaloriListesi,gunListesi) # type'ı zip gösterir.
ziplenmisListe=list(zip(yemekListesi,kaloriListesi,gunListesi))

for eleman in ziplenmisListe:
    print(type(eleman)) #type'ı tuple'dir.

## İleri Seviye Listeler ##

listeOrnegi=[]
benimString="Mustafa Emir Ata"

for harf in benimString:
    listeOrnegi.append(harf)
print(listeOrnegi)

yeniString="mustafa emir ata"
yeniListeOrnegi=[elemaan for elemaan in yeniString]
print(yeniListeOrnegi)

ikinciListeOrnegi=[numara*5 for numara in list(range(0,10))]
print(ikinciListeOrnegi)