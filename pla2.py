#!/usr/bin/env python

# Getting file descriptors

f = open('sample', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')

# Getting input and processing

class card (object):
    def __init__(self, a = 0,b = 0,c = 0):
        self.C = a
        self.S = b
        self.T = c
    def bonus(self):
        return self.C
    def score(self):
        return self.S
    def turns(self):
        return self.T
    def __lt__(self, other):
        return self.score() < other.score()

Turns = 1
Score = 0
    
def process(deck, hand):
    global Turns
    global Score
    def play(card):
        global Turns
        global Score
        Turns += card.turns() -1
        Score += card.score()
        while True:
            if (card.bonus() == 0) or (len(deck) == 0):
                break
            else:
                hand.append(deck[0])
                deck.remove(deck[0])
    hand.sort() 
    while Turns != 0:
        for card in hand:
            if card.turns() != 0:
                play(card)
                hand.remove(card)
        if len(hand) == 0:
            break
        hand.sort()  
        play(hand.pop())
        hand.sort()
    else:
        return Score
        
NumCases = int(f.readline().rstrip())
CaseNum = 0
N = 0
M = 0
deck = []
hand = []

while CaseNum != NumCases:
    N = int(f.readline().rstrip())
    i = 0
    while i != N:
        l = f.readline().rstrip()
        a = int(l.split()[0])
        b = int(l.split()[1])
        c = int(l.split()[2])
        hand.append(card(a,b,c))
        i += 1
    i = 0
    M = int(f.readline().rstrip())
    while i != M:
        l = f.readline().rstrip()
        deck.append(card(int(l.split()[0]), int(l.split()[1]), int(l.split()[2])))
        i += 1
    s.write("Case #%d: %s\n"%(CaseNum+1,process(deck,hand)))
    CaseNum += 1       


# Closing files

f.close()
s.close()