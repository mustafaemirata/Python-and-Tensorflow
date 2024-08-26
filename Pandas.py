import numpy as np
import pandas as pd
#SERIES

benimSozlugum={"Atıl":50, "Zeynep":40,"Mehmet":30}
a=pd.Series(benimSozlugum)
print(a)
print("----")

benimYaslarim=[50,40,30]
benimIsimlerim=["Atıl","Zeynep","Mehmet"]
yas= pd.Series(benimYaslarim)
print(yas)

print("------")

total= pd.Series(benimYaslarim,benimIsimlerim)
print(total)

print("-----")

#Aynı Şey!!!
di= pd.Series(data=benimYaslarim,index=benimIsimlerim)
print(di)

print("------")
aa=numpyDizisi=np.array([50,40,30])
print(aa)
cevrilmis= pd.Series(numpyDizisi)
print(cevrilmis)
print("*****")
birlestirilmis=pd.Series(numpyDizisi,benimIsimlerim)
print(birlestirilmis)