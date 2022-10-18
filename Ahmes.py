# |---------- Algoritmo di Ahmes ----------|
# Questo programma mima il modo di calcolare 
# la moltiplicazione come facevano gli egizi
# circa 3000 anni fa.
# |----------------------------------------|

# Funzione Ahmes
def ahmes(a: int ,b: int ,r=0):
    if a == 1:
        if r == 0:
            print(f"Termine algoritmo: \t \t {a} * {b}")
        else:
            print(f"Termine algoritmo: \t \t {a} * {b} + {r}")
        return b + r
    elif a % 2 == 0:
        if r == 0:
            print(f"{a} è pari: \t \t {a}/2 * 2*{b} = ")
        else:
            print(f"{a} è pari: \t \t {a}/2 * 2*{b} + {r} = ")
        return ahmes(a//2, 2*b, r)
    else:
        if r == 0:
            print(f"{a} è dispari: \t \t ({a} - 1) * {b} + {b}= ")
        else:
            print(f"{a} è dispari: \t \t ({a} - 1) * {b} + {b+r} = ")
        return ahmes(a-1, b, b+r)

# Input di dati dall'esterno

a = input("Inserisci il primo numero: ")        #input carica una stringa
a = int(a)
b = input("Inserisci il secondo numero: ")      #input carica una stringa
b = int(b)
r = 0

#while a >= 1:
#    if a == 1:
#        print(f"il risultato di {a}*{b} + {r} = {b+r}")
#        break
#    elif a % 2 == 0:
#        print(f"{a}/2 * 2*{b} + {r} = ", end="")
#        a = a//2
#        b = 2*b
#    else:
#        print(f"({a}-1) * {b} + {b+r} = ", end="")
#        a = a - 1
#        r = r + b
        
print(f"Il risultato è {ahmes(a,b)}")

        