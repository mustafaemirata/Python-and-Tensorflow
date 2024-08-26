import pandas as pd
import numpy as np

sozluk1={"İsim":["Ahmet","Mehmet","Zeynep","Atıl"],"Spor":["Koşu","Yüzme","Koşu","Basketbol"]
         ,"Kalori":[100,200,300,400]}
dataFrame1=pd.DataFrame(sozluk1,index=[0,1,2,3])
print(dataFrame1)

sozluk2={"İsim":["Osman","Levet","Aslı","Fatma"],"Spor":["Koşu","Yüzme","Koşu","Basketbol"]
         ,"Kalori":[200,300,40,300]}
dataFrame2=pd.DataFrame(sozluk2,index=[4,5,6,7])
print(dataFrame2)
print("----------")
sozluk3={"İsim":["Ayşe","Mahmut","Duygu","Nur"],"Spor":["Koşu","Yüzme","Badminton","Tenis"]
         ,"Kalori":[300,400,500,250]}
dataFrame3=pd.DataFrame(sozluk3,index=[8,9,10,11])
print(dataFrame3)
print("---BİRLEŞTİLMİŞ HALİ---")
## CONCATENATION ##
print(pd.concat([dataFrame1,dataFrame2,dataFrame3]))
print("---------MERGE---------")

###MERGE### (kaynaştırma)

mergeSozluk1={"İsim":["Ahmet","Mehmet","Zeynep","Atıl"],
              "Spor":["Koşu","Yüzme","Koşu","Basketbol"]}

mergeDataFrame1=pd.DataFrame(mergeSozluk1)

mergeSozluk2={"İsim":["Ahmet","Mehmet","Zeynep","Atıl"],
             "Kalori":[100,200,150,250]}

mergeDataFrame2=pd.DataFrame(mergeSozluk2)
print(pd.merge(mergeDataFrame1,mergeDataFrame2,on="İsim"))
print("----------")
maasSozluk={"İsim":["Atıl","Zeynep","Mehmet","Ahmet"],
            "Departman":["Yazılım","Satış","Pazarlama","Yazılım"],
            "Maaş":[200,300,400,500]}
maasDataFrame=pd.DataFrame(maasSozluk)
print(maasDataFrame)
print("--------")
#Sadece Departman kolonundaki verilerin isimini getirir.
print(maasDataFrame["Departman"])

#Departman sütunundakileri tek bir defa getirtir.aynı olanları getirmez.
print(maasDataFrame["Departman"].unique())

#Kaç tane uniq departman olduğunu yazdırır.
print(maasDataFrame["Departman"].nunique())

#Neynden kaç tane olduğuunu ekrana yazdırma
print(maasDataFrame["Departman"].value_counts())

def bruttenNete(maas):
    return maas * 0.66
print(maasDataFrame["Maaş"].apply(bruttenNete))

#Eksik değer olup olmadığını kontrol etme
print(maasDataFrame.isnull())
print("----------YENİ----------")
yeniBirVeri =\
    {
    "Karakter Sınıfı": ["South Park", "South Park", "Simpson", "Simpson","Simpson"],
    "Karakter İsmi": ["Cartman", "Kenny", "Homer", "Bart","Bart"],
    "Karakter Yaş":[9,10,50,20,10]
    }

karakterDF=pd.DataFrame(yeniBirVeri)
print(karakterDF)
print("*******")
#TABLOLARI AYIRDI SINFILANDIRMA YAPTI
print(karakterDF.pivot_table(values="Karakter Yaş",index={"Karakter Sınıfı","Karakter İsmi"},aggfunc=np.sum))
#Eğer bir isimden 2 tane aynı değer varsa ikisini toplayıp ortalamasını aldırır.
#aggfunc=np.sum dersek ikisini toplayıp tabloya yazdırır.