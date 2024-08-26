def bolmeIslemi(numara):
    return (numara/2)
print(bolmeIslemi(20))

benimListem=[1,2,3,4,5,6,7,8,9,10]
yeniListe=[]

for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))
print(yeniListe)

## MAP ## (Sadece fonksiyon adı)
a= list (map(bolmeIslemi,benimListem))
print(a)

## İçindeki harfi kontrol etme
def kontrolFonksiyonu(string):
    return "a"in string
print(kontrolFonksiyonu("Emiar"))

## Liste içerisindeki kelimelerde map kullanımıyla kontrol etme
stringListesi=["Mustafa","Emir","Ata","Mehemt","Ahmet","Levent","Hakan"]
a=list(map(kontrolFonksiyonu,stringListesi))
print(a)
print(a.count(False))

## Filter
## İçerisinde a olan kelimeleri gösteriri. Yani değeri true olanları verir.
b=list(filter(kontrolFonksiyonu,stringListesi))
print(b)

## Lambda (Fonksiyonu tek satırda yazma)
carpma=lambda numara: numara*3
print(carpma(10))

ornekListesi=[10,20,30]
c= list(map(lambda numara : numara*4,ornekListesi))
print(c)