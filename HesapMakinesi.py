def hesapla(a,b,islem):

    if islem not in "+-*/":
        return "Lütfen şu işlemlerden birini seçiniz. :+-*/"


    if islem=="+":
        return str(a) + " + " + str(b) + " = " + str(a + b)
    if islem=="-":
        return (str(a) + " - " + str(b) + " = " + str(a - b))
    if islem=="*":
        return (str(a) + " * " + str(b) + " = " + str(a * b))
    if islem=="/":
        return (str(a) + " / " + str(b) + " = " + str(a / b))

while True:
    try:
        a = float(input("İlk sayıyı giriniz."))
        b = float(input("İkinci sayıyı giriniz."))
        islem = input("İşleminizi seçiniz: + , -, *, /")
        snuc = hesapla(a, b, islem)
        print(snuc)
    except:
        print("Lütfen sayıları düzgün girin.")
