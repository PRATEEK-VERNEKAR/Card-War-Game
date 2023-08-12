from random import shuffle
import pandas as pd
import matplotlib.pyplot as plt

suit=('Hearts','Diamonds','Spades','Clubs')
rank=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,suit,rank):
        # global values
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank+' of '+self.suit

class Deck:
    def __init__(self):
        self.total_cards=[]
        for i in suit:
            for j in rank:
                self.total_cards.append(Card(i,j))

    def shuffle(self):
        shuffle(self.total_cards)

    def deal_one(self):
        return self.total_cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.player_cards=[]

    def remove_one(self):
        return self.player_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.player_cards.extend(new_cards)
        else:
            self.player_cards.append(new_cards)

    def __str__(self):
        return self.name+" has "+str(len(self.player_cards))+" cards."

d=Deck()
d.shuffle()

print("*********WELCOME TO 'CARD-WAR' GAME***********\n")

n1=input("PLAYER 1 name :- ")
n2=input("PLAYER 2 name :- ")
print('\n')
p1=Player(n1)
p2=Player(n2)

for i in range(52):
    if i%2==0:
        p1.add_cards(d.deal_one())
    else:
        p2.add_cards(d.deal_one())

war=False

lst1=[26]
lst2=[26]

while len(p1.player_cards)!=0 and len(p2.player_cards)!=0:
    if war==False:
        l2=[]
    choice1=input(f'{p1.name}\tp-Place Your Card\tx-Exit\n')
    if choice1.lower()=='x' :
        print('\n')
        print(f'{p1.name} Exited\n{p2.name} is the winner!')
        print('\n')
        break
    else:
        a=p1.remove_one()
        print(a)
        print('\n')
    choice2=input(f'{p2.name}\tp-Place Your Card\tx-Exit\n')
    if choice2.lower()=='x' :
        print('\n')
        print(f'{p2.name} Exited\n{p1.name} is the winner!')
        print('\n')
        break
    else:
        b=p2.remove_one()
        print(b)
        print('\n')

    if a.value>b.value:
        l=[]
        l.append(a)
        l.append(b)
        l2.extend(l)
        p1.add_cards(l2)
        print(p1)
        print(p2)
        print('\n','*'*100,'\n')
        lst1.append(len(p1.player_cards))
        lst2.append(len(p2.player_cards))
        if war==True:
            war=False

    if b.value>a.value:
        l=[]
        l.append(a)
        l.append(b)
        l2.extend(l)
        p2.add_cards(l2)
        print(p1)
        print(p2)
        print('\n','*'*100,'\n')
        lst1.append(len(p1.player_cards))
        lst2.append(len(p2.player_cards))
        if war==True:
            war=False

    l1=[]
    l1.extend(l2)

    if a.value==b.value:
        if len(p1.player_cards)<6:
            print('\n')
            print(f'{p1.name} is left with no cards\nCongratulations {p2.name} is the winner')
            print('\n')
            break
        if len(p2.player_cards)<6:
            print('\n')
            print(f'{p2.name} is left with no cards\nCongratulations {p1.name} is the winner')
            print('\n')
            break

        war=True
        print("WAAARRRRRR!!!")
        l2=[]
        if l1!=[]:
            l2.extend(l1)
        l2.append(a)
        l2.append(b)
        for i in range(5):
            l2.append(p1.remove_one())
            l2.append(p2.remove_one())

print('\n')

if len(p1.player_cards)<=0:
    print(f'{p1.name} is left with no cards\nCongratulations {p2.name} is the winner')
elif len(p2.player_cards)<=0:
    print(f'{p2.name} is left with no cards\nCongratulations {p1.name} is the winner')

print('\n')

print("GAME OVER!!")

print('\n')

round=[]
for i in range(1,len(lst1)+1):
  round.append(i)

plt.plot(round,lst1,label='Player-1')
plt.plot(round,lst2,label='Player-2')
plt.xlabel('No. of rounds')
plt.ylabel('Cards remaining')
plt.title('Player-1 v/s Player-2')
plt.legend()

plt.show()
