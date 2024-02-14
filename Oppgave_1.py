# OPPGAVE 1
# Velger å løse denne oppgaven ved å lage en funksjon som tar inn en vilkårlig .txt-fil og outputer hver linje reversert.


def txt_file_reverser(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    reversed_lines_list = []
    file_content_list = file_content.split('\n')

    for line in file_content_list:
        reversed_line = line[::-1]
        reversed_lines_list.append(reversed_line)

    reversed_content = '\n'.join(reversed_lines_list)

    return f"Reversert .txt-fil:\n{reversed_content}"

# Erstatt 'Oppgave 1/file.txt' med stien til 'file.txt' hvis koden ikke fungerer.
file_path = 'Oppgave 1/file.txt'
print(txt_file_reverser(file_path))
