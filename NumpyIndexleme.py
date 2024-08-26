import numpy as np
#benimDizim1=np.arange(0,15,8) #0'dan 15E kadar 8'er atlayarak dizi oluştur.
benimDizim=np.arange(0,15,)
print(benimDizim)

print(benimDizim[3:5])
print("------")

#3'ten başlayıp 8'e kadar dahil olmayan ama elemanları -5 yapmak.
benimDizim[3:8]=-5
print(benimDizim)
print("--------")

baskaDizi=np.arange(0,24)
print(baskaDizi)
print("------")
silicingDizisi = baskaDizi[4:9]
print(silicingDizisi)

#silicingDizisi=700
#print(silicingDizisi) #type int olur

silicingDizisi[:]=700 #tüm elemanları 700'e eşitler.
print(silicingDizisi)

print("------")

ornekDizi=np.arange(0,24)
print(ornekDizi)

ornekDiziKopyasi = ornekDizi.copy()
print(ornekDiziKopyasi)