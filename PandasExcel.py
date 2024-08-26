import pandas as pd
import numpy as np

# Excel dosyasını oku ve DataFrame oluştur
dataFrame = pd.read_excel("maas.xlsx")

# DataFrame'i yazdır
print(dataFrame)
print("*****")
a=dataFrame.dropna()
print(a)
#Excel'e kayıt etme
a.to_excel("yenimaas.xlsx")
