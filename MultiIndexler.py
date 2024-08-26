import pandas as pd
import numpy as np

ilkIndexler=["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
icIndexler=["Homer","Bart","Marge","Cartman","Kenny","Kyle"]

birlesmisIndex=list(zip(ilkIndexler,icIndexler))
print(birlesmisIndex)

birlesmisIndex=pd.MultiIndex.from_tuples(birlesmisIndex)
print(birlesmisIndex)

benimCizgiFilmListem=[[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
benimCizgiFilmNumpDizisi=np.array(benimCizgiFilmListem)
cizgiFilmDataFrame=pd.DataFrame(benimCizgiFilmListem,index=birlesmisIndex,columns=["Yas","Meslek"])
print(cizgiFilmDataFrame)
#Sadece girilen grubu getirir.
print(cizgiFilmDataFrame.loc["Simpson"])
cizgiFilmDataFrame.index.names=["Film Adı","İsim",]
print(cizgiFilmDataFrame)