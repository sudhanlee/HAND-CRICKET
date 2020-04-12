#This game was developed by SURIYANANDAN AND RAMSUDHAN
#Thank you for playing this game
#If you have any problem contact us through github 'C-YBERBOT'
#THANKYOU
import random
import time as t

def batting():
    print('PLAYER BATS FIRST')
    t.sleep(3)
    player=0
    while 'true':   
        a=int(input('Enter No B/W 1 To 10==>'))
        print('.........................')
        if a>0 and a<11:
            z=random.randint(1,10)  
            if a!=z:
                player+=a
                print('PC PUT==>',z)
                print('PLAYER\'S SCORE==>',player)
                t.sleep(1)
                print('.........................')
            elif a==z:
                print('OUT!')
                print('SCORE==>',player)
                print('TARGET IS',player+1)
                t.sleep(1)
                break
        else:
            print('Invaid input')
    print('.........................')
    print('PLAYER BOWLS')
    t.sleep(3)
    comp=0
    while comp<(player+1):
        a=int(input('Enter No B/W 1 To 10==>'))
        print('.........................')
        if a>0 and a<11:
            z=random.randint(1,10)
            if a!=z:
                comp+=z
                print('PC PUT==>',z)
                print('PC\'S SCORE==>',comp)
                t.sleep(1)
                print('.........................')
            elif a==z:
                print('OUT')
                t.sleep(1)
                break
        else:
            print('Invalid input')
    print('Calculating Result...')
    t.sleep(3)
    if player<comp:
        print('PC WON THE MATCH')
    elif player>comp:
        print('PLAYER WON THE MATCH')
    else:
        print('THE MATCH IS DRAW')

#-----------------------------------------


def bowling():
    print('PC BATS FIRST')
    t.sleep(3)
    comp=0
    while 'true':   
        a=int(input('Enter No B/W 1 To 10==>'))
        print('.........................')
        if a>0 and a<11:
            z=random.randint(1,10)  
            if a!=z:
                comp+=z
                print('PC PUT==>',z)
                print('PC\'S SCORE==>',comp)
                t.sleep(1)
                print('.........................')
            elif a==z:
                print('OUT!')
                print('SCORE==>',comp)
                print('TARGET IS',comp+1)
                t.sleep(1)
                break
        else:
            print('Invaid input')
    print('.........................')
    print('PLAYER BATS')
    t.sleep(3)
    player=0
    while player<(comp+1):
        a=int(input('Enter No B/W 1 To 10==>'))
        print('.........................')
        if a>0 and a<11:
            z=random.randint(1,10)
            if a!=z:
                player+=a
                print('PC PUT==>',z)
                print('PLAYER\'S SCORE',player)
                t.sleep(1)
                print('.........................')
            elif a==z:
                print('OUT')
                t.sleep(1)
                break
        else:
            print('Invalid input')
    print('Calculating Result...')
    t.sleep(3)
    if player<comp:
        print('PC WON THE MATCH')
    elif player>comp:
        print('PLAYER WON THE MATCH')
    else:
        print('THE MATCH IS DRAW')
#-----------------------------------------

print('WELCOME TO THE GAME')
def game():
    a=input('ODD OR EVEN>')
    b=int(input('Enter No B/W 1 To 10==>'))
    z=random.randint(1,10)
    if a=='odd' or 'ODD' or 'Odd':
        if(b+z)%2!=0:
            print('PLAYER WON THE TOSS')
            c=input('BATING(bat) OR BOWLING(bowl)')
            if c=='bat':
                batting()
            elif c=='bowl':
                bowling()
        elif (b+z)%2==0:
            print('PLAYER LOSS THE TOSS')
            bowling()
    elif a=='even' or 'EVEN' or 'Even':
        if(b+z)%2==0:
            print('PLAYER WON THE TOSS')
            c=input('BATING(bat) OR BOWLING(bowl)')
            if c=='bat':
                batting()
            elif c=='bowl':
                bowling()
        elif (b+z)%2!=0:
            print('PLAYER LOSS THE TOSS')
            batting()
game()
#----------------------------------------------------

x=input('PLAY AGAIN(y/n)')
if x=='y' or 'Y':
    game()
else:
    exit()
