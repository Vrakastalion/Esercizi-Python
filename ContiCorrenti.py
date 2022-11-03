class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto
        
class ContoCorrente(Conto):

    def __init__ (self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo
        print(f"Inizializzo il conto {self.conto} di proprietà di {self.nome} per un importo di {self.__saldo}€")
        print("")
          
    def preleva(self, importo: float):
        print(f"Ho prelevato dal conto {self.conto} di proprietà di {self.nome} per un importo di {importo}€")
        self.__saldo -= importo
        print(f"Il saldo attuale è di {self.__saldo}€")
        print("")
        
    def deposita(self, importo):
        print(f"Ho depositato sul conto {self.conto} di proprietà di {self.nome} per un importo di {importo}€")
        self.__saldo += importo
        print(f"Il saldo attuale è di {self.__saldo}€")
        print("")

    def descrizione(self):
        print(f"DESCRIZIONE: Il conto {self.conto} di proprietà di {self.nome} ha un saldo attuale di {self.__saldo}€")
        print("")
        
    @property
    def saldo(self):
        print("-Procedura GET-")
        return self.__saldo
    
    @saldo.setter
    def saldo(self, importo):
        print("-Procedura SETTER-")
        self.preleva(self.__saldo)
        self.deposita(importo)

class GestioneContiCorrenti:

    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)        
        print(f"Bonifico dal conto {sorgente.conto} al conto {destinazione.conto} di importo {importo} eseguito!")
        print(f"I nuovi importi sono: ")
        print(f"{sorgente.conto}: Saldo: {sorgente.saldo}")
        print(f"{destinazione.conto}: Saldo: {destinazione.saldo}")
        print("")
        
# Main

c1 = ContoCorrente("Cristian", "0001A", 15000)
c2 = ContoCorrente("Tristano", "0002A", 5000)
c3 = ContoCorrente("Ubaldo", "0017C", 85000)

GestioneContiCorrenti.bonifico(c1, c2, 3_000)
