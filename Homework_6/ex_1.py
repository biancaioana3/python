import os
import sys


def citeste_si_afiseaza_fisiere(director, extensie):
    try:
        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul '{director}' nu există.")

        if not extensie.startswith("."):
            raise ValueError(
                "Extensia fișierului este invalidă. Ar trebui să înceapă cu un punct (de exemplu, '.txt').")

        print(f"Căutare fișiere cu extensia '{extensie}' în directorul: {director}")

        for nume_fisier in os.listdir(director):
            if nume_fisier.endswith(extensie):
                cale_fisier = os.path.join(director, nume_fisier)

                try:
                    with open(cale_fisier, 'r') as fisier:
                        continut_fisier = fisier.read()
                        print(f"\nConținutul lui {nume_fisier}:\n{continut_fisier}")

                except Exception as eroare_fisier:
                    print(f"Eroare la citirea fișierului {nume_fisier}: {eroare_fisier}")

    except Exception as e:
        print(f"Eroare: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilizare: python script.py <cale_director> <extensie_fisier>")
    else:
        cale_director = sys.argv[1]
        extensie_fisier = sys.argv[2]
        citeste_si_afiseaza_fisiere(cale_director, extensie_fisier)
