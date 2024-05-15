# Classe padre con costruttore delle opere
class Item:
    def __init__ (self,title,is_checked_out):
        self.title = title
        self.is_checked_out = is_checked_out

    # funzione con controllo booleano sul check
      
    def check_out(self):
        if self.checked_out_== True:
            
            print(f"{self.title} è stato controllato.")

        else:
            print(f"{self.title} è da controllare.")

    # funzione con controllo booleano sul prestito

    def return_item(self):

        if self.checked_out_== True:
            print(f"{self.title} è stato restituito.")
            
        else:
            raise ValueError(f"{self.title} non è stato preso in prestito.")
        
# classi figlie che ereditano da Item 

class Book(Item):
    def __init__(self, title,is_checked_out):
        super().__init__(title,is_checked_out)


class Journal(Item):
    def __init__(self, title, is_checked_out):
        super().__init__(title, is_checked_out)


# funzione di controllo principale

def main():
    book1 = Item("Il nome della rosa", "Disponibile")
    book2 = Item("Oppenheimer","In prestito")
    journal1 = Item("Focus","In prestito")
    journal2 = Item("Physical review","Disponibile")

    try:
        book1.return_item()  
    except ValueError as e:
        print(f"Anomalia: {e}")

    

    book1.check_out(Item)  
    book2.check_out(Item)  

    book1.return_item()    
    book2.return_item()  

    journal1.check_out(Item)
    journal2.check_out(Item)

    journal1.return_item()
    journal2.return_item()

if __name__ == "__main__":
    main()


   





   

   


