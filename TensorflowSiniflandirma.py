import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
dataFrame= pd.read_excel("maliciousornot.xlsx")
print(dataFrame)
print("-----")
print(dataFrame.describe())
print("*********")
print(dataFrame.corr()["Type"].sort_values()) #Type'a göre olumlu7olumsuzluk

sbn.countplot(x="Type",data=dataFrame) #Kaç tane 0 kaç tane 1 var onu gösterir.

dataFrame.corr()["Type"].sort_values().plot(kind="bar")


plt.show()