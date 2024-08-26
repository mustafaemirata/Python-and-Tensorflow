import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

# Excel dosyasını oku
dataFrame = pd.read_excel("merc.xlsx")

# Veriyi yazdır
print(dataFrame)

# Temel istatistiksel bilgileri yazdır
print(dataFrame.describe())

# Eksik değerleri kontrol et
print(dataFrame.isnull().sum())

# 'price' sütununun dağılım grafiğini çiz
plt.figure(figsize=(7, 5))  # Grafik boyutunu ayarla
sbn.displot(dataFrame["price"], kde=True)  # kde=True ile yoğunluk eğrisi ekle
plt.title("Price Dağılımı")
plt.xlabel("Fiyat")
plt.ylabel("Frekans")
#plt.show()

# 'year' sütununun sayım grafiğini çiz
plt.figure(figsize=(10, 6))  # Yeni grafik boyutunu ayarla
sbn.countplot(x=dataFrame["year"])
#plt.show()
print("------")
print(dataFrame.corr())
print("------")
print(dataFrame.corr()["price"].sort_values())
sbn.scatterplot(x="mileage",y="price",data=dataFrame)
plt.show()
print("-----")
yuzdeDoksanDokuzDf=dataFrame.sort_values("price",ascending=False).iloc[131:]#En yülksek fiyaatı en yukarıda gösterme , false
print(yuzdeDoksanDokuzDf.describe())

plt.figure(figsize=(7,5))
sbn.displot(yuzdeDoksanDokuzDf["price"])
#plt.show()

print(dataFrame.groupby("year").mean()["price"]) #Yılların ortalamasını alma işlemi.
print("----------")
print(yuzdeDoksanDokuzDf.groupby("year").mean()["price"])
a=dataFrame[dataFrame.year!=1970].groupby("year").mean()["price"]
print(a)  #1970'i listeden atma işlemi
dataFrame=dataFrame.drop("transmission",axis=1)

#transmission sütununu kaldırma işlemi.

y=dataFrame["price"].values
x=dataFrame.drop("price",axis=1).values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3,random_state=10)
from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)
from tensorflow.keras.models import Sequential