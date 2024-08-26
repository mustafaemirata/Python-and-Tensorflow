benimString="Mustafa Emir Ata"
print(benimString[3])

## Immutability
## benimString[0]="B"  Değişmezlik mevcut. Kod çalışmaz.

benimListem=[10,20,30,40]
print(type(benimListem))

benimNumaram=10
benimDigerNumaram=90
benimNumaraListem=[benimNumaram,benimDigerNumaram]
print(benimNumaraListem)

benimListem[0]=100
print(benimListem)

## isteye öge ekleme / Eklenen eleman listenin sonuna eklenir.
benimListem.append(50)
print(benimListem)

############  LİSTE METOTLARI  ############

## Son elemanı kaldırma
benimListem.pop()
## 50yi kaldırdı.
print(benimListem)

## İstenen elemanı listeden çıkartma
benimListem.remove(20)
print(benimListem)

## Count : belirli elemandan listede kaç tane var
print(benimListem.count(30))

benimStringListem=["Mustafa","Mehmet","Kerem","Ali"]
benimDigerListem=["Ahmet","Mahmut","Atlas"]
print(benimDigerListem[2])
benimToplamListem=benimStringListem+benimDigerListem
print(benimToplamListem)

##Reverse : Listeyi tersine çevirme
benimToplamListem.reverse()
print(benimToplamListem)

###### İleri Seviye Listeler ######

karisikListe=[1,2,3.5,"atıl",9]
sonucum=karisikListe[2]
print(type(sonucum)) ## Integer gösterir.

nestedList=[1,5,"a",4,[6,"z"]]
print(nestedList[4]) ## Listenin içindeki listeyi yazar.
alinacakHarf=nestedList[4][1]  ## z harfine erişmek için.
print(alinacakHarf)

karmasikListe = [[1,2,3,["a","b"],50]]

print(nestedList[2:])