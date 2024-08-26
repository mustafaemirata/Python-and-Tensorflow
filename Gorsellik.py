import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pyt

numpyDizisi1=np.linspace(0,10,20)
numpyDizisi2=numpyDizisi1 ** 2

(benimFigur, benimEksen)=pyt.subplots()
benimEksen.plot(numpyDizisi1,numpyDizisi2,color="#3A95A8",alpha=0.3) #alpha saydamlık katar.
benimEksen.plot(numpyDizisi2,numpyDizisi1,color="#C96F23")
plt.show()

(yeniFigur, yeniEksen)=plt.subplots()
yeniEksen.plot(numpyDizisi1,numpyDizisi1+2,color="b",linewidth=5)#linewidth kalınlık verir.
yeniEksen.plot(numpyDizisi1,numpyDizisi1+3,color="g")
yeniEksen.plot(numpyDizisi1,numpyDizisi1+4,color="#C96F23",linestyle="-.") #-.  çizgi ve noktalı  : noktalı çizer
yeniEksen.plot(numpyDizisi1,numpyDizisi1+5,color="#C96F23",linestyle=":")
yeniEksen.plot(numpyDizisi1,numpyDizisi1+6,color="#C96F23",linestyle="--")

yeniEksen.plot(numpyDizisi1,numpyDizisi1+7,color="#000000",linestyle="--",marker="o",markersize=4,markerfacecolor="r")
yeniEksen.plot(numpyDizisi1,numpyDizisi1+8,color="#000000",linestyle="--",marker="+",markersize=16,markerfacecolor="r")
plt.show()

##SCATTER
#Veriler dağııtlmış bir şekilde gelir.
plt.scatter(numpyDizisi1,numpyDizisi2)
plt.show()

#Histogram

yeniDizi=np.random.randint(0,100,50) #0 ile 100 arasında random 50 veri
plt.hist(yeniDizi)
plt.show()

#BOXPLOT

plt.boxplot(yeniDizi)
plt.show()