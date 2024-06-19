class Student:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def display_details(self):
        print(f"Student: {self.nome} {self.cognome}, Matricola: {self.matricola}")

class Course:
    def __init__(self,corso):
        self.corso = corso
        self.voti = []

    def votazione(self, voto):

        if voto >= 60/100:
            print("Passato")

        else:
            print("Da ripetere")

    def add_students(self, new):

        if new == True:
            print("Riempi modulo per il corso prescelto")

        else:
            print("Non fare niente")

    def aggiungi_voto(self,voto):
        if 0 <= voto <= 100:
            self.voti.append(voto)
        else:
            print("Voto fuori range")
    
    def media_voti(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)


    def display_details(self):
        print(f"Course: {self.corso}")
        print(f"Voti: {self.voti}")
        print(f"Media_voti: {self.media_voti():.2f}")

# Example usage:
student = Student("Andrea","Diliberto",56987)
course = Course("IT")

# Adding grades
course.aggiungi_voto(80)
course.aggiungi_voto(90)
course.aggiungi_voto(75)


# Display course details and average grade
student.display_details()
course.display_details()



