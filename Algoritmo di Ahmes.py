# Funzione di calcolo ricorsiva

def ahmes(a,b,r=0):
    if a == 1:
        if r == 0:
            print(f"{a} è 1: \t \t {a} * {b}",)
        else:
            print(f"{a} è 1: \t \t {a} * {b} + {r}")
        return b + r
    elif a % 2 == 0:        
        if r == 0:
            print(f"{a} è pari: \t {a}/2 * 2*{b} = ")
        else:
            print(f"{a} è pari: \t {a}/2 * 2*{b} + {r} = ")
        return ahmes(a//2, 2*b, r)
    else:
        if r == 0:
            print(f"{a} è dispari: \t ({a} - 1) * {b} + {b}= ")
        else:
            print(f"{a} è dispari: \t ({a} - 1) * {b} + {r+b} = ")
        return ahmes((a-1),b,r+b)

# Intestazione

print("Il programma propone il metodo egizio di calcolo della moltiplicazione presente nel papiro di Ahmes")

# Input dei due numeri

a = input("Inserisci il primo numero intero: ")
a = int(a)
b = input("Inserisci il secondo numero intero: ")
b = int(b)

# Calcolo

print(f"Il risultato è {ahmes(a,b)}")



