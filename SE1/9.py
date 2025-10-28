start = int(input())
end = int(input())
day = ""

dayCount = (start + end) % 7
if dayCount == 1:
    day = "Понеделник"
elif dayCount== 2:
    day = "Вторник"
elif dayCount == 3:
    day = "Сряда"
elif dayCount == 4:
    day = "Четвъртък"
elif dayCount == 5:
    day = "Петък"
elif dayCount == 6:
    day = "Събота"
else :
    day = "Неделя"
print(day)