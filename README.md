# Esercizi-Python
## Esercizi corso Python - ITS Alto Adriatico

I file qui presenti sono le soluzioni degli esercizi rilasciati nel corso di Python per QZER e CPER all'interno della formazione del 2° anno presso l'ITS Alto Adriatico di Pordenone (PN)

## Esercizi base:
**1) Algoritmo di Ahmes**

*KEY: String interpolation, IF...ELIF...ELSE, Ciclo WHILE, Ciclo FOR, Pensiero algoritmico*

Si richiede di realizzare un programma che segua l'algoritmo di Ahmes (1650 a.C.) per la moltiplicazione. Gli egizi volevano ragionare in seno alla semplice moltiplicazione per 2 e la divisione per 2 oltre che alle somme di qualsiasi genere e in questo algoritmo spiegano come poter fare la moltiplicazione di due numeri avendo in mente solo queste succitate possibilità. Si tratta di seguire le tracce a noi lasciate, ovvero il programma riceve in input due numeri interi a, b e procede come segue:
  - Se $a=1$ allora $a * b = b$ (REGOLA DI STOP)
  - Se $a$ è pari allora $a * b = (\frac{a}{2}) * (2 * b)$ (REGOLA PARI)
  - Se $a$ è dispari allora $a * b = (a-1) * b + b$ (REGOLA DISPARI)

L'algoritmo procede con l'applicazione delle regole fino al gaggiungimento della regola di stop. Si richiede una visualizzazione del procedimento seguito dall'algoritmo.

**2) Calcolo MCM, mcd**

*KEY: String interpolation, IF...ELIF...ELSE, Ciclo WHILE, Ciclo FOR, calcoli modulari*

Si richiede di calcolare, dati due numeri interi positivi $x, y$ , il loro Massimo Comune Divisore (MCD) e il loro minimo comune multiplo (mcm) seguendo l'algoritmo di Euclide, ovvero:
  - Sia $a_i = b_i * q_i + r_i$ dove $a_0 = max(x,y)$ e $b_0 = min(x,y)$ e $r_i$ è tale che $0 \leq r_i \leq_i$
  - $a_{i+1} = b_i$ e $b_{i+1} = r_i$
  - Si prosegue sino a che $r_i = 0$ 

Si richiede una visualizzazione del procedimento seguito dall'algoritmo.

**3) Torre di Hanoi**

*KEY: funzione ricorsiva, azione di gruppo simmetrico* $S_n$

Si richiede di gestire e visualizzare il gioco della [Torre di Hanoi](https://it.wikipedia.org/wiki/Torre_di_Hanoi) con d-dischi mediante un algoritmo strutturato

**4) Codice di Cesare**

*KEY: cryptanalisi base, algebra modulare*

Seguendo il metodo utilizzato da Cesare e formalizzato come $y \equiv x - a \mod 26$ dove $a$ è lo spostamento a destra o sinistra delle parole ed $x$ e $y$ sono le $26$ lettere dell'alfabeto moderno codificate come codice ASCII ("a" minuscola è uguale a $60$), inserire una frase e permetterne la codifica. Scrivere inoltre un programma per la decodifica sapendo $a$.

Quanto è complesso trovare una decodifica senza sapere che il metodo di cryptazione è quello di Cesare?

**5) Numero troppo grande**

*KEY: funzioni ricorsive, rappresentazioni numeriche, algebra modulare*

Scrivere un programma che scriva il risultato preciso di una potenza $a^b$ dove $a,b \geq 10^5$ senza usare la scrittura scientifica e senza approssimazione.

**6) Radice quadrata babilonese**

*KEY: funzioni ricorsive, approssimazione, distanza, vicinanza, numeri in formato frazionario*

Seguendo l'esempio babilonese scrivere un programma che richieda un errore massimo $\epsilon$ e un numero intero $\alpha$ e poi ne calcoli la radice quadrata con un errore minore dell'errore massimo inserito. L'algoritmo da seguire è:

$$\begin{cases}
\displaystyle x_n = \frac{1}{2} \cdot \left( x_{n-1}+ \frac{\alpha}{x_{x-1}} \right) \\
x_0 = 1
\end{cases}$$

Dopo aver calcolaro il valore float, proporre un metodo per visualizzare il risultato in formato frazionario.

**7) Zeri di un polinomio**

*KEY: approssimazione, continuità*

Si richiede uno script per il calcolo degli zeri di un polinomio mediante il [metodo di bisezione](https://it.wikipedia.org/wiki/Metodo_della_bisezione). Il polinomio deve essere inserito dall'utente e può essere un polinomio al massimo di grado 5. L'errore massimo da commettere deve essere inserito dall'utente.

Proporre poi uno script per il [metodo di Newton](https://it.wikipedia.org/wiki/Metodo_delle_tangenti) e confrontare il tempo ed i passaggi necessari per trovare le soluzioni.

**8) Metodo Moltecarlo**

*KEY: statistica*

Proporre uno script per giocare a [battaglia navale](https://it.wikipedia.org/wiki/Battaglia_navale_(gioco)) usando il principio che sottostà al [metodo Montecarlo](https://it.wikipedia.org/wiki/Metodo_Monte_Carlo) tra un giocatore umano ed un agente programmato. Proporre una battaglia tra due agenti che usano il medesimo metodo. E' possibile determinare quale sia la strategia di posizionamento migliore? 


## Progetti ed esercitazioni complesse

**1) Starfire**

Scrivere uno script per gestire efficacemente la creazione dell'universo per il gioco [Galactic Starfire](https://boardgamegeek.com/boardgame/7539/galactic-starfire) -originale gioco del 1979- seguendo il regolamento.

**2) Briscola**

Scrivere uno script completo per la gestione del gioco della [Briscola](https://it.wikipedia.org/wiki/Briscola). La partita si svolge tra un giocatore umano ed un agente programmato. Si deve proporre uno script per ciascuno degli agenti:
- Agente S: avendo 3 carte in mano, sceglie a caso tra le 3
- Agente G: conosce tutto del gioco (disposizione del mazzo, carte in mano sia sue che dell'avversario)
- Agente M: segue una strategia preimpostata e determinata (da costruire, ma che sia una via di mezzo tra S e G)

E' possibile proporre una policy di agenti (chiamiamola Mx) che scali la strategia da S a G? Come? 

**3) HEX**

Scrivere uno script completo per la gestione del gioco [HEX](https://it.wikipedia.org/wiki/Hex_(gioco)). La partita si svolge tra un giocatore umano ed un agente programmato. Si deve proporre uno script per un agente che sia scalato in 5 possibili difficoltà dove 1 è la difficoltà più semplice e 5 la più difficile.
