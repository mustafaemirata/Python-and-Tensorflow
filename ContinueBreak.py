benimListem=[5,10,15,20,25,30]

for numara in benimListem:
    print(numara/5)  # // ile tam sayı şeklinde böler

#15'ten sonrasını yazdırmadı. (Break)
for numara in benimListem:
    if numara==15:
        break
    print(numara)

#Girilen elemanı yaazdırmadan diğer elemanlara geçti.
for numara in benimListem:
    if numara==15:
        continue
    print(numara)

# Sonrada doldurmak için kullanılır. Hata vermeden pas geçer.
for numara in benimListem:
    pass