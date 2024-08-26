def toplama(numara1,numara2):
    return numara1+numara2

x=int(input("İlk syaıyı giriniz."))
y=int(input("İkinci sayıyı giriniz."))
print(toplama(x,y))

##  TRY & EXCEPT & ELSE & FINALLY

while True:
    try:
        benimInt=int(input("Numaranızı giriniz:  "))
    except:
        print("Lütfen gerçekten numara giriniz.")
        continue
    else:
        print("Teşekkürler!")
        break
    finally:
        print("finally çağırıldı!")