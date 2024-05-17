import math

def calcola_radice_quadrata():
    try:
        numero = float(input("Inserisci un numero: "))
        if numero < 0:
            raise ValueError("Il numero deve essere positivo.")
        radice_quadrata = math.sqrt(numero)
        print(f"La radice quadrata di {numero} è {radice_quadrata}")
    except ValueError as ve:
        print(f"Input errato: {ve}")

if __name__ == "__main__":
    calcola_radice_quadrata()
