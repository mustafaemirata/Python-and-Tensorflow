isimString="Mustafa Emir Ata"
## Indexleme
print(isimString[10])

## 2: ile kaçıncı indexten itibaren yazdıracağını gösterir.
yeniStirng="0123456789"
print(yeniStirng[2:])

## :2 2.indexe kadar al 2 dahil olmayacak
print(yeniStirng[:2])

##SlICING

gelenVeri="AhmetinYasi65"
print(gelenVeri[-2:]) ## sondan 2 karakteri yazdırma

## verilenler arasındaki karakterleri yazdırma
print(gelenVeri[2:4]) ## 2den başla 4te dur alma

##Step Szie
print(gelenVeri[::]) ##Stringin kendisini gösterir.
print(gelenVeri[::2]) ## değişkeni ikişer atlayarak yazdırdı.

##Cümleyi tersine Çevirme
print(gelenVeri[::-1])