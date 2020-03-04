#totalNumItemsAtStart = 400
#numItemsPerPlayerAtStart = totalNumItemsAtStart/numPlayers
#sumOfPlayerBets = kennyBet + robot1Bet + robot2Bet + robot3Bet
#playerNames[numPlayers] = {"Kenny", "robot1", "robot2", "robot3"}
###comment- comments without the word comment are for pieces of unused code

###comment- import random is used to allow random int functions
import random

###comment- initializes variables to zero or null etc and gets number and names of players as well as who is and isnt a human 
print("how many players should there be?:")
numPlayers = int(input())
i=0
identity = []
name = []
humanPlayer = []
botCount = 0
humanCount = 0
while(i < numPlayers):
    print("is player", i+1 ,"a person or a bot")
    copyInput = input()
    identity.append(copyInput)
    print("what is the name of player", i+1)
    copyInput = input()
    name.append(copyInput)
    i=i+1
i=0

#print(random.randint(1,2))

#determines how many human and non human players there are
while(i < numPlayers):
    if((identity[i] == "bot")or(identity[i] == "b")or(identity[i] == "robot")):
        humanPlayer.append(False)
        botCount = botCount+1
    if((identity[i] == "person")or(identity[i] == "human")or(identity[i] == "p")or(identity[i] == "h")):
        humanPlayer.append(True)
        humanCount = humanCount+1
    i=i+1
print("There are",numPlayers,"players", humanCount, "of which are human and",botCount, "are artificial")    


#Game START
print("type help for more instructions at any time")
print("How much would you like to bet?")
while(1==1):
    copyInput = input()
    try:
        int(copyInput)
        print("good number")
    except ValueError:
        if(copyInput == "help"):
            print("for a list of commands type commands")
            print("for an overview of the game type rules")
        if(copyInput == "commands"):
            print("type help for more instructions at any time")
            print("type commands at any time for a list of commands")
            print("type the amount you would like to bet during your turn to place a bet")
            print("type back to go back to the previous screen")

