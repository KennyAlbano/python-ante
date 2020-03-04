humanCount = 0
botCount = 0
names = []
def getNumPlayers():
    global humanCount
    global botCount
    print("How many human players are there?")
    try:
        humanCount = int(input())
    except ValueError:
        print("you must type in a whole number for each player type")
        getNumPlayers()
    print("Do you wish to compete with non human players as well?")
    botsIncluded = input()
    if(botsIncluded == "yes" or botsIncluded == "y"):
        print("How many non humans are playing?")
        try:
            botCount = int(input())
        except ValueError:
            print("you must type in a whole number for the number of eeach player type")
            getNumPlayers()
    else:
        botCount = 0
    if(humanCount + botCount < 3):
        print("You must have a total of at least 3 players")
        getNumPlayers()
        
def getNames():    
    i=0
    while(i<humanCount):
        print("What is the name of player", i+1)    
        names.append(input())
        i+=1
        
def gameStart():
    i=0
    print(names [i],"please place your bet or type help at any time")
    while(1==1):
        copyInput = input()
        try:
            int(copyInput)
            placedBet(copyInput)
        except ValueError:
            if(copyInput == "help"):
                print("for a list of commands type commands")
                print("for an overview of the game type rules")
            if(copyInput == "commands"):
                print("type help for more instructions at any time")
                print("type commands at any time for a list of commands")
                print("type the amount you would like to bet during your turn to place a bet")
                print("type back to go back to the previous screen")
            if(copyInput == "rules" or copyInput == "about" or copyInput == "about game" or copyInput == "game summary" or copyInput == "summary"):
                print("This game is called ante and was invented by Kenny Albano during")
                print("the winter of 2020. The objective of the game is to win more")
                print("money than the other players.")
def placedBet(bet):
    print(bet)

#main
getNumPlayers()
getNames()
gameStart()
