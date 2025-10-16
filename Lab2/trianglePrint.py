# Трета задача
number = int(input("number="))

for i in range(1, number+1):
    row = ""
    for j in range(1, i+1):
        row+="*"
    print(row)
