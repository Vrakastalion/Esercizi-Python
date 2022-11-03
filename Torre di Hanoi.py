# Progetto Torre di Hanoi
# Si tratta di disegnare la soluzione ottimale per la Torre di Hanoi con d-dischi

# Funzione che 'disegna' la Torre in base alla lista
def disegna(lista):
    global d
    vuoto = list()
    for k in range(d):
        vuoto.append(" ")
    A = [vuoto.copy(),vuoto.copy(),vuoto.copy()]
    
    for i in range(3):
        try:
            for j in range(d):
                A[i][j] = str(lista[i][j]+1)    # Il +1 serve a visualizzare i dischi da 1 a d
        except IndexError:
            A[i][j] = " "
        A[i].sort(reverse=True)                 # Questo serve per visualizzare i numeri dei dischi dall'alto verso il basso 
            
    print( " A  B  C ")
    print( "---------")
    
    for k in range(d):
        print(f" {A[0][k]}  {A[1][k]}  {A[2][k]} ", end = "")
        print("")  
    
# L'idea del main è quella di partire da una lista di liste che rappresentano
# i dischi presenti sui pioli
def main(d):
    
    # Inizializzazione Lista di liste:
    # Lista di liste con la prima lista inserita come comprehension
    # con valori da 1 a d
    pila = [i for i in range(d)]
    hanoi = [pila.copy(),[],[]]             # Da ricordarsi la condivisione!
    
    # Conteggio dei passi effettuati
    counter = 0
    
    # Condizione di fine algoritmo
    fine = True
    
    # Due tipologie di mosse:
    # Questa soluzione deve emergere da un'ANALISI preliminare del problema. 
    mossepari = [[0,1],[0,2],[1,2]]
    mossedispari = [[0,2],[0,1],[1,2]]
    
    # Determinazione mosse
    if d % 2 == 0:
        mosse = mossepari
    else:
        mosse = mossedispari   
        
    # Ciclo che ripete le 3 mosse fino al raggiungimento dell'obiettivo     
    while fine:
        for i in mosse:
            
            disegna(hanoi)
            print("")
            
            # Condizione di fine algoritmo
            if hanoi[2] == pila:        # Da ricordarsi la condivisione!
                fine = False
                break
            # Incrementa il counter per visualizzare il numero di passi effettuato.
            # Attenzione al posizionamento
            counter += 1
            
            # Da determinare la sorgente 'sorg' dello scambio e la destinazione 'dest'
            sorg = i[0]
            dest = i[1]
            
            cond1 = bool(hanoi[sorg])
            cond2 = bool(hanoi[dest])
            
            if cond1:                   # Questo è vero se la lista hanoi[sorg] non è vuota
                if cond2:               # Questo è vero se la lista hanoi[dest] non è vuota
                    x = hanoi[sorg][0]
                    y = hanoi[dest][0]
                    if x > y:
                        sorg = i[1]
                        dest = i[0]
            # Qui si arriva se hanoi[sorg] è vuota e ragionevolmente hanoi[dest] non è vuota
            # L'unico caso in cui sono entrambe vuote è quando il gioco è finito
            # ma l'ho considerato nella condizione di fine immediatamente sopra
            else:                       
                sorg = i[1]
                dest = i[0]
            
            print(f"Sorgente: {sorg + 1}a pila", end="; ")
            print(f"Destinazione: {dest + 1}a pila")
            
            # Carico il valore da spostare
            x = hanoi[sorg][0]
            print(f"L'elemento che sposto è il disco {x+1}")
            
            # Spostamento:
            # Cancello il primo elemento dalla pila sorgente
            del hanoi[sorg][0]
            
            #Aggiungo l'elemento alla pila destinatario come primo elemento
            hanoi[dest].insert(0,x)
    
    # Alla fine stampo il numero di passi
    print(f"Il processo termina in {counter} passi")        
            

# Introduzione           
print("/---------- Torre di Hanoi ----------/")
print("Il programma propone e visualizza la")
print("risoluzione dei una Torre di Hanoi a d-dischi")
print("")

# Input inserito dall'utente

d = input("Inserisci il numero di dischi che desideri: ")
d = int(d)

main(d)

