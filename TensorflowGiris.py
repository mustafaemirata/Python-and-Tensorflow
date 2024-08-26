import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sbn

# Örnek veri oluştur
x_train = np.random.rand(100, 3) * 1000  # 100 örnek, 3 özellik (1000'e kadar rastgele değerler)
y_train = np.random.rand(100, 1) * 1000  # 100 örnek, 1 çıkış
x_test = np.random.rand(20, 3) * 1000    # Test verisi

# Verileri ölçeklendir
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

print(x_train)  # Veriler 0 ve 1 arasına getirildi

# Modeli oluştur
model = Sequential()
model.add(Dense(4, activation="relu", input_shape=(x_train.shape[1],)))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(1))

# Modeli derle
model.compile(optimizer="rmsprop", loss="mse")

# Modeli eğit
history = model.fit(x_train, y_train, epochs=250, verbose=1)

# Kayıp değerlerini çiz
loss = history.history["loss"]
plt.figure(figsize=(10, 6))
sbn.lineplot(x=range(len(loss)), y=loss)
plt.title("Model Kayıp Değeri (Loss) - Epoklar")
plt.xlabel("Epok")
plt.ylabel("Kayıp (Loss)")
plt.show()

# Model ile tahmin yap
y_pred = model.predict(x_test)

# Tahminleri ve gerçekteki değerleri karşılaştır
print("Tahmin Edilen Değerler:", y_pred[:5])
# Örnek olarak ilk 5 tahmini yazdırıyoruz
