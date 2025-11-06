budget = float(input("Budget:"))
season = input("Season:")
destination = ""
percent = 0
reservation = ""
if season == "summer":
    reservation = "Camp"
else:
    reservation = "Hotel"
if budget <= 100:
    destination = "Bulgaria"
    if (season == "summer"):
        percent = 0.3
    if (season == "winter"):
        percent = 0.7
elif budget <= 1000:
    destination = "Balkans"
    if (season == "summer"):
        percent = 0.4
    if (season == "winter"):
        percent = 0.8
else:
    reservation = "Hotel"
    destination = "Europe"
    percent = 0.9


print(f"Somewhere in %s" %(destination))
print(f"%s - %.2f" %(reservation, budget * percent))