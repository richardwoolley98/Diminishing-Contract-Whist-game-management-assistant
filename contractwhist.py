#Diminishing Contract Whist is a card game whose rules can be read here: https://boardgamegeek.com/thread/850446/contract-whist.
#Due to taking place over several rounds, the bets and running scores need to be written down to be kept track of.
#This python code automates this tracking system, as well as randomly selecting a trump card for each round of play.
#The code works for any number of players or rounds, but bear in mind that a deck of cards only has 52 cards, so a group of 6 players cannot play 10 rounds as they'd require 60 cards for the first round.
#The last player to guess (the dealer) in each round is prompted with what value they cannot guess, but this is purely instructive and the code will continue normally if that value is indeed entered.

import random
players = []
suits = ["Hearts","Diamonds","Spades","Clubs"]
def numplayers(n=input("How many players are playing? ")): #user chooses the number of names to be added
    numplay = int(n)
    for s in range(1,numplay+1):
        players.append(input("Name of player " + str(s) + ": ")) #user adds the actual names to a list for the players
    return players 

dealers = [] #empty list to be filled with the dealers for each round
def play(r=input("How many rounds do you want to play? ")): #user chooses the number of rounds to be played
    print(" ")
    rounds = int(r)
    roundsinit = int(r) 
    rotatingplayers = players 
    lenplayers = len(players)
    scores = [0]*lenplayers
    c = 0
    while c < roundsinit:
        if c < lenplayers:
            dealers.append(players[c])
            c += 1
        elif c < 2*lenplayers:
            dealers.append(players[c-lenplayers])
            c += 1
        elif c < 3*lenplayers:
            dealers.append(players[c-(2*lenplayers)])
            c += 1
        elif c < 4*lenplayers:
            dealers.append(players[c-(3*lenplayers)])
            c += 1
    while rounds > 0:
        if rounds == roundsinit:
            dealerround = players[-1]
        else:
            dealerround = dealers[(roundsinit - 1) - rounds]
        guesser = dealers[(roundsinit - rounds)]
        if rounds > 1:
            print(dealerround + " should deal " + str(rounds) + " cards to each player, and the first player to guess is " + guesser + "\n")
        else:
            print(dealerround + " should deal " + str(rounds) + " card to each player, and the first player to guess is " + guesser + "\n")
        trump = random.choice(suits)
        if rounds == roundsinit:
            print("Start the " + str((roundsinit + 1) - rounds) +"st round! The trump suit is " + trump + "\n")
        elif rounds == (roundsinit - 1):
            print("Start the " + str((roundsinit + 1) - rounds) +"nd round! The trump suit is " + trump + "\n")
        elif rounds == (roundsinit - 2):
            print("Start the " + str((roundsinit + 1) - rounds) +"rd round! The trump suit is " + trump + "\n")
        else:
            print("Start the " + str((roundsinit + 1) - rounds) +"th round! The trump suit is " + trump + "\n")
        guesses = []
        j = players.index(guesser)
        sums = 0
        count = 0
        exclude = 0
        while j < len(players) + players.index(guesser):
            if count == 4:
                guess = int(input("How many hands does " + players[j % len(players)] + " expect to win? Cannot say " + str(exclude) + ". "))
            else:
                guess = int(input("How many hands does " + players[j % len(players)] + " expect to win? "))
            guesses.append(guess)
            j += 1
            count += 1
            sums += guess
            exclude = rounds - sums
        print(" ")
        actuals = []
        i = players.index(guesser)
        while i < len(players) + players.index(guesser):
            actuals.append(int(input("How many hands did " + players[i % len(players)] + " win? ")))
            i+=1
        for i in range(0,lenplayers):
            if guesses[i] == actuals[i]:
                scores[i] = scores[i] + 10 + actuals[i]
            else:
                scores[i] = scores[i] + actuals[i]
        print(" ")
        if rounds > 1:
            for i in range(0,lenplayers):
                print(players[i] + " has a current score of " + str(scores[i]))
            scores.append(scores.pop(0))
            rotatingplayers.append(rotatingplayers.pop(0))
            print(" ")
            print("______________________________________________________________________________________")
        else:
            for i in range(0,lenplayers):
                print(players[i] + " has a final score of " + str(scores[i]))
        rounds += -1

def main():
    numplayers()
    play()

if __name__ == "__main__":
    main()
