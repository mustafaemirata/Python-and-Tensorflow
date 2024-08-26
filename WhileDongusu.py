x=0

#while x<10:
#   print(x)
#  x=x+1
benimListem=[1,2,3,4,5]
#print(benimListem.pop()) #Çıkarılan elemanı yazdırır.
#benimListem.pop()
#print(benimListem)

while 3 in benimListem:
    print("3 listenin içerisinde")
    benimListem.pop()
numara=0

while numara <5:
    if numara==4:
        break
    print(numara)
    numara=numara+1

yeniDegisken=0
while yeniDegisken<15:
    # print("Yeni Degiskenin Güncel Değeri: "+str(yeniDegisken))
    print(f"yeniDegisken'in güncel değeri: {yeniDegisken}")# f:format. Süslü parantez içine yazılanı kod olarak anlamasını sağlar.
    yeniDegisken=yeniDegisken+1