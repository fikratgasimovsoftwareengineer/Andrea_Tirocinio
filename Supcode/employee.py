class Employee:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.registro_ore = []
        self.registro_progetti = []

    def assign_projects(self, nome_progetto):
        self.nome_progetto = nome_progetto
        self.registro_progetti.append(nome_progetto)

    def record_working_hours(self,ore):
        self.registro_ore.append(ore)

       
class Manager(Employee):
    def __init__(self, nome, cognome,carica):
        super().__init__(nome, cognome)
        self.carica = carica

    
    def assegno_manager(self, bonus_produzione):
        self.bonus_produzione = bonus_produzione
        return self.bonus_produzione


class Technician(Employee):

    def __init__(self, nome, cognome,mansione):
        super().__init__(nome, cognome)
        self.mansione = mansione

    def paga(self, paga_oraria):
        self.paga_oraria = paga_oraria
        return paga_oraria
    
def main():
    

    nome = "Arturo"
    cognome = "Dellera"
    carica = "Caporeparto"
    bonus = 70
    capo = Manager(nome, cognome, carica)
    print(f"Manager: {capo.nome} {capo.cognome}, Carica: {capo.carica}")
    print(f"Bonus produzione: {capo.assegno_manager(bonus)}")

    nome2 = "Piero"
    cognome2 = "Rossano"
    mansione = "tornitore"
    paga = 50
    tecnico = Technician(nome2, cognome2, mansione)
    print(f"Technician: {tecnico.nome} {tecnico.cognome}, Mansione: {tecnico.mansione}")
    print(f"Paga oraria: {tecnico.paga(paga)}")
    

if __name__ == "__main__" :
    main()