class Product:

    def __init__(self, nome_prodotto, dimensioni):
        self.nome_prodotto = nome_prodotto
        self.dimensioni = dimensioni

class Cart(Product):

    def __init__(self, nome_prodotto, dimensioni, d_acquisto, acquisto):
        super().__init__(nome_prodotto, dimensioni)
        self.d_acquisto = d_acquisto
        self.acquisto = acquisto
        self.acquisti = []

    def add_products(self, acquisto):
        self.acquisti.append(acquisto)

    def remove_products(self, acquisto):
        self.acquisti.remove(acquisto)

   

class Order(Product):
    
    def __init__(self, nome_prodotto, dimensioni,prezzo):
        super().__init__(nome_prodotto, dimensioni)
        self.prezzo = prezzo

    def add_purchase(self, acquistato):
        self.acquistato = acquistato
    
        return self.nome_prodotto * self.acquistato * self.prezzo
    
   
def main():

    nome = "aereo"
    dimensioni = 100
    d_acquisto = 160287
    acquisto = "eseguito"
    ord1 = Cart(nome,dimensioni,d_acquisto,acquisto)
    print(f"Ordine : {ord1.nome_prodotto},{ord1.dimensioni}")
    print(f"Ordine : {ord1.d_acquisto},{ord1.acquisto}")

    nome2 = "furgone"
    dimensioni2 = 7
    d_acquisto2 = 201216
    acquisto2 = "non eseguito"
    ord2 = Cart(nome2,dimensioni2,d_acquisto2,acquisto2)
    print(f"Ordine : {ord2.nome_prodotto},{ord2.dimensioni}")
    print(f"Ordine : {ord2.d_acquisto},{ord2.acquisto}")

    prezzo = 300
    prezzo2 = 1
    ord1 = Order(nome, dimensioni, prezzo)
    ord2 = Order(nome2, dimensioni2, prezzo2)
    print(f"{ord1.nome_prodotto},{ord1.dimensioni},{ord1.prezzo}")
    print(f"{ord2.nome_prodotto},{ord2.dimensioni},{ord2.prezzo}")
    
if __name__ == "__main__":
    main()