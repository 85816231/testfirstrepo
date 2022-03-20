# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:24:40 2022

@author: 86180
"""
from random import shuffle

class Card:
    suits = ["♠",
    "♡",
    "♢",
    "♣"]

    values = [None, None, "2", "3",
    "4", "5", "6", "7",
    "8", "9", "10",
    "J", "Q",
    "K", "A" ]

    def __init__(self, v, s):
        """suit 和 value 的值都为整型数"""
        self.value = v
        self.suit = s    
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False    
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False    
    
    def __repr__(self):
        v = self.suits[self.suit]+self.values[self.value]
        return v
    
class Deck:
    def __init__(self):
        self.cards = []
    
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)    
    
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    
    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
    
    
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    
    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        
        win = self.winner(self.p1, self.p2)
        
        print("War is over. {} wins".format(win))
    
    
    def winner(self, p1, p2):
        print("{} won {} times, and {} won {} times".format(p1.name, p1.wins, p2.name, p2.wins))
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


game = Game()
game.play_game()

# print(deck.cards)
# print(deck.cards[2]>deck.cards[1])

#打印牌面的情况，按花色前后打印
# for idx, x in enumerate(Card.suits):
#     #print(x)
#     for i in range(52):
#         #print(deck.cards[i].suit)
#         if deck.cards[i].suit==idx:
#             print(deck.cards[i], end=' ')
#     print()

#打印每个选手的牌面情况
# index = 0
# for i in range(52):
#     if i%13==0:
#         index +=1
#         print("第{}个人的牌是：".format(index), end="")
#     print(deck.cards[i], end=" ")
#     if (i+1)%13==0:
#         print()
        

