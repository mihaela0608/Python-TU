text = input("Text:")
dictionary = dict()
for letter in text:
    value = list(text)
    value.remove(letter)
    currentText = ""
    for i in value:
        currentText+=i
    dictionary[letter] = currentText
print(dictionary)