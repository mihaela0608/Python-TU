words = list(input("Text: ").split(" "))
longest = ""
shortest = ""
for word in words:
    if(shortest == ""):
        shortest = word
    if(len(word) > len(longest)):
        longest = word
    if(len(shortest) > len(word)):
        shortest = word

words.remove(longest)
words.remove(shortest)

for i in words:
    print(i, end = " ")