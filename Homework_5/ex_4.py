import os
import sys


def numara_fisiere_cu_extensii(director):
    try:
        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul '{director}' nu există.")

        if not os.access(director, os.R_OK):
            raise PermissionError(f"Nu poți citi din directorul '{director}'.")

        fisiere = os.listdir(director)

        if not fisiere:
            print(f"Directorul '{director}' este gol.")
            return

        contor_extensii = {}

        for fisier in fisiere:
            extensie = os.path.splitext(fisier)[1].lower()

            contor_extensii[extensie] = contor_extensii.get(extensie, 0) + 1

        print("Contorizare fișiere cu extensii:")
        for extensie, numar in contor_extensii.items():
            print(f"{extensie}: {numar} fișiere")

    except Exception as e:
        print(f"Eroare: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: python script.py <cale_director>")
    else:
        cale_director = sys.argv[1]
        numara_fisiere_cu_extensii(cale_director)
