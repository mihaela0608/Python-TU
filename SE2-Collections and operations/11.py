dictionary = dict()

command = input()

while(command != "Exit"):
    data = command.split(" ")
    command = data[0]
    if (command == "Add"):
        eng = command[1]
        bg = command[2]
        
    command = input()
