import os
import sys


def calculeaza_dimensiunea_totala(director):
    try:
        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul '{director}' nu există.")

        dimensiune_totala = 0

        for radacina, subdirectoare, fisiere in os.walk(director):
            for fisier in fisiere:
                cale_fisier = os.path.join(radacina, fisier)

                try:
                    dimensiune_totala += os.path.getsize(cale_fisier)

                except Exception as eroare_dimensiune:
                    print(f"Eroare la calcularea dimensiunii fișierului {cale_fisier}: {eroare_dimensiune}")

        print(f"Dimensiunea totală a fișierelor în directorul '{director}': {dimensiune_totala} octeți")

    except Exception as e:
        print(f"Eroare: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: python script.py <cale_director>")
    else:
        cale_director = sys.argv[1]
        calculeaza_dimensiunea_totala(cale_director)
