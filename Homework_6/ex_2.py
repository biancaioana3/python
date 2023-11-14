import os


def redenumește_fișiere(director):
    try:
        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul '{director}' nu există.")

        fișiere = os.listdir(director)

        fișiere.sort()

        for index, nume_fișier in enumerate(fișiere, start=1):
            cale_veche = os.path.join(director, nume_fișier)
            cale_nouă = os.path.join(director, f"fișier{index}{os.path.splitext(nume_fișier)[1]}")

            os.rename(cale_veche, cale_nouă)
            print(f"Redenumire reușită: {cale_veche} -> {cale_nouă}")

    except Exception as e:
        print(f"Eroare: {e}")


if __name__ == "__main__":
    director = input("Introdu calea către director: ")
    redenumește_fișiere(director)
