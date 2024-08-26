import pandas as pd
import numpy as np
sozlukVerisi={"İstanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"İzmir":[40,39,38]}
havaDurumuDataFrame=pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)

#Non olan bütün satırları siliyor
print(havaDurumuDataFrame.dropna())
#NaN olmayan tek kolonu getirmke
print(havaDurumuDataFrame.dropna(axis=0))  #1 deyhnce kolonları 0 deyince sırayı alır.

yeniVeri={"İstanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"İzmir":[40,39,38],"Antalya":[45,np.nan,np.nan]}
yeniDataFrame=pd.DataFrame(yeniVeri)
print(yeniDataFrame)
print("------")
#Sütunlarda (axis=1) 2den fazla nan olanları siliyor
print(yeniDataFrame.dropna(axis=1,thresh=2))

#Boş olanları doldurmak.

print(yeniDataFrame.fillna(20))

##GROUPBY##
maasSozlugu={"Departman":["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
             "Çalışan İsmi":["Ahmet","Mehmet","Atıl","Burak","Zeynep","Fatma"],
             "Maaş":[100,1250,200,300,400,500]}
maasDataFrame=pd.DataFrame(maasSozlugu)
print(maasDataFrame)

grupObjesi=maasDataFrame.groupby("Departman")
#Hangi departmanda kaç kişi var
print(grupObjesi.count())

#Departmöanlardaki ortalama maaşları yazdırır.
print(grupObjesi.mean())

#Hangi departmanda maaşı max olan kişinin adı ve maaşını yazdırır.
print(grupObjesi.max())

#Ortalamasını,standart sapmasını, yüzdeliğini,minimum,maximum bilgilerini gösterir.
print(grupObjesi.describe())