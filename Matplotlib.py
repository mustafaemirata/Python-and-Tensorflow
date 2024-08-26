import numpy as np
import matplotlib.pyplot as plt

# Veriler
yasListesi = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
kiloListesi = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]

# Listeleri numpy dizilerine dönüştürme
nuumpyYasListesi = np.array(yasListesi)
numpyKiloListesi = np.array(kiloListesi)

# 0 ile 10 arasında 20 tane ayrı numara oluştur. EŞİT UZAKLIKTA!!
numpyDizisi1 = np.linspace(0, 10, 20)
numpyDizisi2 = numpyDizisi1 ** 3

# 1. Alt grafik
plt.subplot(1, 2, 1)  # 1 satır, 2 sütun, 1. grafik
plt.plot(numpyDizisi1, numpyDizisi2, "r*-")  # Kırmızı yıldız işaretli çizgi
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')
plt.title('İlk Grafik')

# 2. Alt grafik
plt.subplot(1, 2, 2)  # 1 satır, 2 sütun, 2. grafik
plt.plot(numpyDizisi2, numpyDizisi1, "g--")  # Yeşil kesik çizgi
plt.xlabel('Y Ekseni')
plt.ylabel('X Ekseni')
plt.title('İkinci Grafik')

# Alt grafikleri göster
plt.show()

# Özel figür oluşturma
benimFigure = plt.figure()

# Özel eksen ekleme
figureAxes = benimFigure.add_axes([0.1, 0.1, 0.8, 0.8])  # [sol, alt, genişlik, yükseklik]
figureAxes.plot(numpyDizisi1, numpyDizisi2, "g")  # Yeşil çizgi
figureAxes.set_xlabel("X Ekseni Veri ismi")
figureAxes.set_ylabel("Y Ekseni Veri ismi")
figureAxes.set_title("Grafik Başlığı")

# Özel figürü göster
plt.show()

yeniFigur=plt.figure(dpi=100)  #dpi çözünürlüğü verir.
yeniEksen=yeniFigur.add_axes([0.1,0.1,0.9,0.9])
yeniEksen.plot(numpyDizisi1,numpyDizisi1 **2,label="numpyDizisi ** 2")
yeniEksen.plot(numpyDizisi1,numpyDizisi1**3,label="numpyDizisi **3")
yeniEksen.legend()
plt.show()
#Kayıt oluşturur
yeniFigur.savefig("benimFigure.png",dpi=200)