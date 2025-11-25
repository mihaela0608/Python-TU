def newText(text, *args):
    result = ""
    for i in args:
        result+=text[i]
    print(result)

newText("I am Mihaela Bataklieva", 1, 2, 8, 3)