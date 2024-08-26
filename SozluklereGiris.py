## Key Value Pairing (Anahtar Kelime - Değer Eşleşmesi)
benimYemeklerim=["Elma","Karpuz","Muz"]
benimKalorilerim=[100,200,300]

##Dictionary
benimBosluk={"anahtarkelime":"deger"}
print(benimBosluk)

benimYemekKaloriSozlugum={"elma":100 , "karpuz":200 , "muz":300}
benimYemekKaloriSozlugum["elma"]=200
print(benimYemekKaloriSozlugum["elma"])

yeniDictionary={"anahtar1" : 100, "anahtar2" : [10,20,30,4,5,"atıl"],"anahtar3" :{"anahtar9" : 4}}
print(yeniDictionary.keys())
print(yeniDictionary.values())

print(yeniDictionary["anahtar2"][5])
print(yeniDictionary["anahtar3"]["anahtar9"])
