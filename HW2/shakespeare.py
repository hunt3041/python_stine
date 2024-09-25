from collections import Counter
import re

def analyze_text(filename='t8.shakespeare.txt'):
    with open(filename, 'r') as file:
        contents = file.read()
        contents = re.sub(r'[\.\!\?\.\,\;\:\t\[\]]', '', contents)
        contents = re.sub(r'[--]', ' ', contents)
        words = contents.split()
        word_count = dict(Counter(words))
        word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    return list(word_count.items())[:25]


word_count = analyze_text()

print(word_count)