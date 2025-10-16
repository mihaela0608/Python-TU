# Първа допълнителна задача
number = int(input("number="))

output = ""

if number == 1:
    output = "Monday"
elif number == 2:
    output = "Tuesday"
elif number == 3:
    output = "Wednesday"
elif number == 4:
    output = "Thursday"
elif number == 5:
    output = "Friday"
elif number == 6:
    output = "Saturday"
elif number == 7:
    output = "Sunday"
else:
    output = "Invalid number!"
print(output)