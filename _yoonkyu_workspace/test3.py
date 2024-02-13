import nltk
nltk.download('punkt')

with open('hamlet.txt', 'r', encoding="utf-8") as file:
    text = file.read()

print(text)