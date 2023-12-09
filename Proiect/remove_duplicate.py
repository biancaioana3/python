import os
import filecmp

def find_duplicate_files(folder):
    # Dicționar pentru a stoca fișierele duplicate
    duplicates = {}

    # Parcurge recursiv fișierele din folder
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            # Compară conținutul fișierului cu altele deja identificate ca fiind duplicate
            for key, value in duplicates.items():
                if filecmp.cmp(file_path, key):
                    duplicates[key].append(file_path)
                    break
            else:
                # Adaugă fișierul în dicționar dacă nu este identificat ca duplicate
                duplicates[file_path] = [file_path]

    # Returnează doar fișierele care au duplicate
    return {key: value for key, value in duplicates.items() if len(value) > 1}

def display_duplicate_files(duplicates):
    print("The following files are identical:")
    for index, (key, value) in enumerate(duplicates.items(), start=1):
        print(f"{index}. {key}")
        for i, file_path in enumerate(value[1:], start=2):
            print(f"   {i}. {file_path}")
    print()

def remove_duplicates(duplicates):
    for key, value in duplicates.items():
        total_files = len(value)
        print(f"Please select the file you want to keep [1..{total_files}] for {key} ? ", end="")
        choice = int(input())
        # Șterge doar fișierul selectat, păstrează celelalte
        for i, file_path in enumerate(value, start=1):
            if i == choice:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            else:
                print(f"Kept: {file_path}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python remove_duplicate.py <folder>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.exists(folder_path):
        print("Folder not found.")
        sys.exit(1)

    duplicates = find_duplicate_files(folder_path)
    if not duplicates:
        print("No duplicate files found.")
        sys.exit(0)

    display_duplicate_files(duplicates)
    remove_duplicates(duplicates)
