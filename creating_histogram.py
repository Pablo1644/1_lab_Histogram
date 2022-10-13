#   PwZn 1 laboratorium
from ascii_graph import Pyasciigraph

words = []
freq_of_words = {}


def delete_punctation_mark(line):
    punct = ".,?!-—…-"
    for ele in line:
        if ele in punct:
            line = line.replace(ele, '')
    return line


def histogram(file_name):
    with open(file_name, encoding="UTF-8") as file:
        for line in file:
            if line == '\n':
                pass
            else:
                line = delete_punctation_mark(line)
                line = line.lower()
                words.extend(line.strip().split(' '))  # one list with all words created
    for element in words:
        if element in freq_of_words.keys():
            freq_of_words[element] = freq_of_words[element] + 1
        else:
            freq_of_words[element] = 1
    del freq_of_words['']


histogram("Kamizelka.txt")
# Posortowanie
sort_orders = sorted(freq_of_words.items(), key=lambda x: x[1], reverse=True)

# Wyswietlenie histogramu
graph = Pyasciigraph()
for line in graph.graph('My Histogram', sort_orders):
    print(line)
