# OPPGAVE 2

import json

def odd_number_remover(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    even_numbers = []

    for number in data:
        if number % 2 == 0:
            even_numbers.append(number)

    return f"Liste med partall:\n{even_numbers}\nSum: {sum(even_numbers)}"

# Erstatt 'Oppgave 2/array.json' med stien til 'array.json' hvis koden ikke fungerer.
file_path = 'Oppgave 2/array.json'
print(odd_number_remover(file_path))