import numpy as np

benimMatrisDizisi=[[10,20,30],[20,30,40],[40,50,60]]
benimMatrisDizim=np.array(benimMatrisDizisi)
print(benimMatrisDizim)

print(benimMatrisDizim[0])
print(benimMatrisDizim[1:,2]) # 1.satırdan sonrasını alıyor ve onların 2.indexlerini getiriyor. 40 ve 60.
print("-------------********----------")
yeniListe=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
yeniMatrix=np.array(yeniListe)
print(yeniMatrix)
print("--------")
print(yeniMatrix[[0,2,4]])  #0.2.ve4.indexteki satırları yazar

print("--------***********-----------")

#OPERASYONLAR

yeniBirDizi=np.random.randint(1,100,20) #1'den 100'e kadar toplam 20 sayı vermek
print(yeniBirDizi)

sonucDizisi=yeniBirDizi>24
print(sonucDizisi)

print(yeniBirDizi[sonucDizisi]) #YyeniBirDizideki elemanalrdan sadece 24'ten büyük olanları yazdırmak

print("*******")

sonDizi=np.arange(0,24)
print(sonDizi)
print(sonDizi+sonDizi) #elemanları kendi arasında toplar, çarpar, çıkarır, böler

print(np.sqrt(sonDizi))
