#importing randint function from random module named r
#importing time module for user interaction
from random import randint as r
import time
#Game starts
print("*************Welcome to BlackJack Game*************")
#here by default there will be 100 rupees given.we have to play this game with this money.
money=100
print("your wallet BALANCE is :100")
print(".........................................................................")

def game(money):
    #here it takes the amount u want to place bet.
    bid=int(input("enter amount u bet : "))
    #computer by deafult gives u two cards.
    print('----->Your cards are :',end='')
    your_cards=[]
    #assiging two cards by using random.
    for i in range(2):
        your_cards.append(r(1,11))
    print(your_cards)
    #computer cards same as above
    com_cards=[]
    com_cards.append(r(1,11))
    print('--->Computer card is ',com_cards)
    #-------------
    choice=True
    sum1=0
    sum2=0
    #loop for extra cards.
    while choice:
        x=input("Do you want another card (yes or no): ").lower()
        if x=='no':
            choice=False
        else:
            your_cards.append(r(1,11))
            print('----->your cards are:',your_cards)
        #stores the sum of your cards.
        sum1=sum(your_cards)
        #if u cross the end(21) marks this will execute.
        if sum1>21:
            print("*----------YOU LOST THE GAME,COMPUTER WINS----------*")
            #your money in wallet will be deducted.
            money = money - bid
            break
    #loop for computer cards.
    if sum1<=21:
        y=len(your_cards)-1
        while y>0:
            com_cards.append(r(1,11))
            print('computers cards are:',com_cards)
            time.sleep(2)
            sum2=sum(com_cards)
            if sum2>21:
                print("*----------YOU WON THE GAME----------*")
                money = money + bid
                break
            if sum2>sum1:
                print("*----------YOU LOST THE GAME,COMPUTER WINS----------*")
                money = money - bid
                break
            if sum2==sum1:
                print("its a tie")
                break
            y=y-1
        if y==0 and sum2<sum1:
            print("*---------YOU WON THE GAME-----------*")
            money = money + bid
            
    print("your balance is:",money)
    return money
y=game(money)
#if you are having +ve balance u are elegile to play the game.
while y >0:
    x=input("Do u want to play again (yes or no) :").lower()
    if x=='no':
        break
    else:
        #sends total amount as input.And again calls the game function.
        y=game(y)
            

