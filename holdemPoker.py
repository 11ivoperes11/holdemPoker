def valCount(handVal):
    
    # implement a dictionary with key and value
        # for every card, add a 
    for i in handVal:

        if handVal == '2' or handVal == '3' or handVal == '4' or handVal == '5' or handVal == '6' or handVal == '7' or handVal == '8' or handVal == '9':
            intVal = int(i)

        if handVal == '2':

        if handVal == '3':
        if handVal == '4':
        if handVal == '5':
        if handVal == '6':
        if handVal == '7':
        if handVal == '8':
        if handVal == '9':
        if handVal == '10':
        if handVal == 'K':
        if handVal == 'Q':
        if handVal == 'J':
        if handVal == 'A':


    return 0    

def suiteCount(handSuite):
    clubCount = 0
    diamondCount = 0
    spadeCount = 0
    heartCount = 0

    for i in handSuite:
        if i == '♠':
            spadeCount = spadeCount + 1
        if i == '♥':
            heartCount = heartCount + 1
        if i == '♣':
            clubCount = clubCount + 1
        if i == '♦':
            diamondCount = diamondCount + 1
    
    print(f"Clubcount: {clubCount}")
    print(f"Diamondcount: {diamondCount}")
    print(f"Spadecount: {spadeCount}")
    print(f"Heartcount: {heartCount}")

    return 0




def handRanking(hand):
    valList = []
    suiteList = []

    for card in hand:               #divide cards into value and suite
        print(card)
        cSuite = card[-1]
        cVal = card[:-1]
        valList.append(cVal)
        suiteList.append(cSuite)
    
    suiteCount(suiteList)
    valCount(valList)
    




def hand():
    hand5Card = ['k♠','10♠','8♠','7♠','5♠']
    return hand5Card           

def playGame():
    myHand = hand()

    myRank = handRanking(myHand)



if __name__ == "__main__":
    play = playGame()
