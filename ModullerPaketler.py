import numpy as np
import matplotlib.pyplot as matplot

## Maaşı 4000 civarında 500 standart sapması olan 1000 tane veri oluşturma
maasListesi = np.random.normal(4000,500,1000)
ortalama= np.mean(maasListesi)
print(ortalama)

matplot.hist(maasListesi,50)
matplot.show()

