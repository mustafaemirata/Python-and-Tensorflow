## SCOPE (KAPSAM)
numara=20
def carpma(rakam):
    numara=10
    return numara*rakam
print(carpma(5))
print(numara)

## LOCAL, ENCLOSING, GLOBAL, BUILT-IN ##
benimAdim="Mustafa" ## Global

def benimFonksiyonum():
    ##  benimAdim="Mahmut"
    ## Enclosing

    def icFonksiyon():
        ##  benimAdim="Ayşe"  Önce buraya bakıyor sonra üste çıkar
        ## Local
        print(benimAdim)
    icFonksiyon()

benimFonksiyonum()
print(benimAdim)

y=10

def yeniFonksiyon(y):
    print(y)
    y=5
    print(y)
    return y
y=yeniFonksiyon(14)
print(y)

y=10
def ornekFonksiyon():
    global y
    y=0
    print(y)
ornekFonksiyon()

