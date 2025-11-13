wordForGuess = "amazing"
wordList = list(wordForGuess)
copied = wordList.copy()
consoleWord = "-"*len(wordForGuess)
tries = 0
allowedTries = len(wordForGuess) + 5
print(consoleWord)

while(tries < allowedTries):
    letter = input("Letter: ")
    while (letter in copied):
        consoleWord = ""
        for i in range(len(wordForGuess)):
            if(letter in copied):
                if(i == wordList.index(letter)):
                    consoleWord+=letter
                    copied.remove(letter)
                else:
                    consoleWord+="-"
            else:
                consoleWord+="-"
        
    print(consoleWord)
    tries+=1
