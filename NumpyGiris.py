import numpy as np

#NUMPY ARRAY

benimListem = [20,30,40]
print(type(benimListem))

a= np.array(benimListem)
print(a)
print(type(a))

matrixListesi=[[10,20,30],[20,30,40],[30,40,50]]
print(np.array(matrixListesi))

#ARANGE
print(np.arange(0,10))

print(np.arange(0,10,2))

#ZEROS (0 oluşturma)
print(np.zeros(5))
#Matriks olarak oluşturma () içi kullanılır
print(np.zeros((2,2)))

#ONES (1 oluşturma)
print(np.ones((3,3)))

#Linspace
print(np.linspace(0,10,20)) # hepsi arasında eşit fark olur. Son eleman yazdırılır.

#EYE
print(np.eye(10)) #Orta çizgi 1

#RANDOM

print(np.random.randn(8))
print(np.random.randn(4,5))
print(np.random.randint(1,20)) #1'den 20'ye kadar herhangi bir değer döndürmek için.
print(np.random.randint(1,10,5)) # 1 ile 10 arasında 10 dahil olmamak üzere 5 eleman yazdırmak.

benimNumpyDizim=np.arange(30)
print(benimNumpyDizim) #0'dan 30'a kadar 30 dahil olmayacak şekilde oluşturur.

benimRandomDizim=np.random.randint(0,10,100) #0'dan 10'e kadar 30 taane random eleman
print(benimRandomDizim)

#NUMPY DİZİ METOTLARI
print("--------------")
print(benimNumpyDizim.reshape(5,6))
print("----------")
print(benimNumpyDizim.max())  #max elemanı yazdırır
print(benimNumpyDizim.min())
print("-------")
print(benimRandomDizim.argmax()) # max eleman kaçıncı indexte bunnu gmösterir.
print("---------")
print(benimNumpyDizim.shape) #şekil uzunluk

