# OPPGAVE 3

import os

def sommer_counter(folder):
    files_w_sommer = 0
    
    for root, subfolders, files in os.walk(folder):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    if 'Sommer' in f.read():
                        files_w_sommer += 1
    
    return files_w_sommer

# Erstatt 'Oppgave 3' med stien til mappen du vil søke gjennom hvis koden ikke fungerer.
folder_path = 'Oppgave 3'
amount = sommer_counter(folder_path)
print(f"Antall .txt-filer som inneholder ordet 'Sommer': {amount}")

