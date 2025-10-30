data = input()
phoneNumbers = {}
while(data != "end"):
    name = data.split(" ")[0]
    phone = data.split(" ")[1]
    if(name in phoneNumbers):
        phoneNumbers[name].add(phone)
    else:
        phoneNumbers[name] = set()
        phoneNumbers[name].add(phone)
    data = input()


for i in phoneNumbers.keys():
    print(f"%s -> %s" %(i, phoneNumbers[i]))