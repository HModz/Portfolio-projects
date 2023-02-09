import json

f = open("morse-code.json")
code = json.loads(f.read())

text = input("Insert text to convert: ").lower()

coded_text = []

for letter in text:
    if letter != " ":
        coded_text.append(code[letter])
    else:
        coded_text.append(" ")

print(" ".join(coded_text))
