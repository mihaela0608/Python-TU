floors = int(input("Floors:"))
rooms = int(input("Rooms: "))
for i in range(floors, 0, -1):
    letter = "A"
    if(i == floors):
        letter = "L"
    elif(i % 2 == 0):
        letter = "O"
    floor = ""
    for f in range(0, rooms+1):
        room = (f"%s%d%d" %(letter, i, f))
        floor+=(f" %s" %(room))
    print(floor)
    
