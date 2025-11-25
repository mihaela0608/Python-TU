def FindDayWinner(winners):
    results = winners.split(" ")
    first = 0
    second = 0
    for winner in results:
        if (winner == "Team1"):
            first+=1
        else:
            second+=1
    
    if first>second:
        print("Team1")
    elif second>first:
        print("Team2")
    else:
        print("Tie")

FindDayWinner(input())