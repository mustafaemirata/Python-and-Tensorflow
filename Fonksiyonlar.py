benimAdim="Mustafa emir Ata"
print(benimAdim.upper())
#help(benimAdim.upper())   Ne işe yaradığını gösterir.

def ilkFonksiyon():
    print("İlk Fonksiyonum")
ilkFonksiyon()

## Input & Return

def merhabaDunya(yazdirilacakIsim):
    print("Merhaba")
    print(yazdirilacakIsim)
merhabaDunya("Dünya")

def merhaba(isim="emir"):
    print("Merhaba")
    print(isim)
## (Değişkene değer yazılmazsa default olarak emir döndürür.
## Eğer değer verilirse onu döndürür.
merhaba("Mustafa")

def toplama(num1,num2):
    sonuc=num1+num2
    print(sonuc)
#toplama(98,54)
#yeniDegisken=toplama(10,20)
#print(yeniDegisken)  #None döndürür.

def dondurmeliToplama(num1,num2):
    return num1+num2
print(dondurmeliToplama(10,20))
yeniSonuc=dondurmeliToplama(15,25)
print(yeniSonuc)

def kontrolFonksiyon(s):
    if s=="emir":
        print("Verdiğiniz string emir")
    else:
        print("Verdiğiniz string başka bir şey.")
kontrolFonksiyon("emir")

## ARGS AND KWARGS ##

def yeniToplama(*args):
    return sum(args)
print(yeniToplama(10,20,30,40,50))

def benimFonksiyonum(*args):
    return(args)
print(benimFonksiyonum(20,30,40)) #NoneType dööndürür. Fonksiyonda return kullanılırsa tuple döndürür.

def ornekFonksiyon(**kwargs):
    return(kwargs)
ornekFonksiyon(muz=100,elma=200,ananas=300) ##Fonksiyonda return kullanılmadığı sürece bir şey döndürmeyeceğinden type'ı NoneType olur.
print(type(ornekFonksiyon())) ## Type'ı dictionary olarak döndürür.

def keyWordKontrolu(**kwargs):
    if "emir" in kwargs:
        print("Emir var")
    else:
        print("Emir yok")
keyWordKontrolu(atıl=70, emir=19, zeynep=98, mehmet=40)