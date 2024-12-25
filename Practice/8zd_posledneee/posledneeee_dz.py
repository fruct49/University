import pymorphy2
from collections import Counter
from translate import Translator

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

morph = pymorphy2.MorphAnalyzer()
words = text.split()
normalized_words = [morph.parse(word.strip('.,!?'))[0].normal_form for word in words]

word_count = Counter(normalized_words)
sorted_word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))

translator = Translator(from_lang="ru", to_lang="en")
translated_words = {word: translator.translate(word) for word in sorted_word_count}

with open('result.txt', 'w', encoding='utf-8') as file:
    for word, translation in translated_words.items():
        count = sorted_word_count[word]
        file.write(f"{word} | {translation} | {count}\n")
