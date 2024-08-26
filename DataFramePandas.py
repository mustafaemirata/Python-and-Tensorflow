import pandas as pd
import numpy as np
#4 satır 3 kolon
data=np.random.randn(4,3)

#Excel tablosu gibi yazdırıyor.
dataFrame=pd.DataFrame(data)
print(dataFrame)

yeniDataFrame=pd.DataFrame(data,index=["Emir","Efe","zEYNEP","aSLI"],columns=["Maas","Yas","Çalışma Saati"])
print(yeniDataFrame)

print(yeniDataFrame["Çalışma Saati"])
#ROW SEÇİLECEKSE

print(yeniDataFrame.loc["zEYNEP"])

#ındex'e gore çağırma
print(yeniDataFrame.iloc[1])

#YENİ KOLON EKLEME
yeniDataFrame["Emeklilik Yasi"]=yeniDataFrame["Yas"]+yeniDataFrame["Yas"]
print(yeniDataFrame)
print("------")
#KOLON SİLME
yeniDataFrame.drop("Emeklilik Yasi", axis=1, inplace=True)
print(yeniDataFrame)

#Girileni satır boyunca siler
print(yeniDataFrame.drop("Emir",axis=0))
print(yeniDataFrame.loc["zEYNEP"]["Yas"])
#Hangileri 0'dan küçük onu gösterir.
print(yeniDataFrame<0)
#Yaşı 0'dan küçük olanı satırcca siler.
print(yeniDataFrame[yeniDataFrame["Yas"]>0])

#Başa indez ekler
print(yeniDataFrame.reset_index())

yeniIndexListesi=["EAs","Ads","Fnb","Bjk"]
yeniDataFrame["Yeni Index"]=yeniIndexListesi
print(yeniDataFrame)

yeniDataFrame=yeniDataFrame.set_index("Yeni Index",inplace=True)
print(yeniDataFrame)

