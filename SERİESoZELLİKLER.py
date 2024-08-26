import pandas as pd

# Creating the Series with proper syntax
a = pd.Series(["Atıl", "Atlas", "Osman"], index=[1, 2, 3])
print(a)

yarismaSonucu1=pd.Series([10,5,1],["Atıl","Atlas","Osman"])
yarismaSonucu2=pd.Series([20,10,8],["Atıl","Atlas","Osman"])
print(yarismaSonucu2)
#Belilenenin kaçıncı data olduğunu belirtir.
print(yarismaSonucu2["Atlas"])

farkliSeries=pd.Series([20,30,40,50],"a","b","c","d")
farkliSeries2=pd.Series([10,5,3,1],"a","c","f","g")

toplam=farkliSeries+farkliSeries2
print(toplam)
