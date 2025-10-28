gender = input("Мъж или жена:")
result = "... кандидат"
if gender == "жена":
    chest = float(input("Гръдна обиколка:"))
    if (chest >= 100):
        result = "Подходящ кандидат"
    else:
        result = "Неподходящ кандидат"
elif gender == "мъж":
    money = float(input("Банкова сметка:"))
    if (money >= 250000):
        result = "Подходящ кандидат"
    else:
        result = "Неподходящ кандидат"
print(result)