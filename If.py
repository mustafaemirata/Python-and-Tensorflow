#if 3 > 4:
#  print("Mustafa Emir Ata")
#print("if koşulunun dışına çıkıldı.")

x=6
y=6
#if x>y:
# print("x, y'den daha büyükmüş.")
    # a=5
    # b=4
    # print(a+b)
#elif y>x:
#  print("y x'ten daha büyükmüş.")
    #else:
# print("y ve x birbirlerine eşittir.")

benimKahramanim=input("Süper kahraman seçiniz.")

if benimKahramanim=="Batman":
    print("Batman seçtiniz.")
elif benimKahramanim=="Superman":
    print("Keşke Batman'i seçseydiniz.")
elif benimKahramanim=="Ironman":
    print("Iron Man kimdir?")
else:
    print("Bunun kim olduğunu bilmiyorum.")

a=10
b=20
c=20

if a>b and b>c:
    print("a, bden büyük ve b de c'den büyük")
elif a<b and b<c:
    print("a, b'den küçük ve b c'den küçük")
else:print("Bu koşullar tutmadı.")

#benimIsım="Mustafa Emir Ata"

#if "Ata"in benimIsım:
    #print("Varmış")
#else:
#  print("yokmuş")

benimSozluk={"muz":100, "elma":150, "karpuz":500}
print(benimSozluk.keys())

if "muz"in benimSozluk.keys():
    print("Sözlükte mevcut.")