grade = float(input())
maxTuition = float(input())
tuition = 0
if grade >= 5.50:
    tuition = maxTuition
elif grade >= 5.00:
    tuition = maxTuition * 0.7
elif grade >= 4.50:
    tuition = maxTuition * 0.5
print(f"Вашата стипендия е: %.2f" %(tuition))
    