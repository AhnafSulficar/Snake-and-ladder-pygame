import pygame
import random
import time 
diceroll=0
pygame.init()

screen= pygame.display.set_mode((1050 ,650))
pygame.display.set_caption("Snake and Ladder")

#background

img1=pygame.image.load("board 2.jpg")
img2=pygame.image.load("dicebcg.png")

#players
r1=pygame.image.load("pins1.png")
b1=pygame.image.load("pins2.png")

roll=pygame.image.load("rollbutton.png")
arrow=pygame.image.load("arrow.png")

button=pygame.Rect(50,60,60,60)

def bck():
    screen.blit(img2,(0,300))
    screen.blit(img1,(450,15))
    screen.blit(roll,(30,50))
    screen.blit(arrow,(130,83))
    
def rplayer(x,y):
    screen.blit(r1,(x,y))
def bplayer(x,y):
    screen.blit(b1,(x,y))
rx=30
ry=150

bx=30
by=260
font0=pygame.font.SysFont("comicsansms",35)
font1=pygame.font.SysFont("comicsansms",25)
font2=pygame.font.SysFont("comicsansms",20)

def picknumber():
    diceroll=random.randint(1,6)
    if diceroll==1:
        dice=pygame.image.load("d1.png")
    if diceroll==2:
        dice=pygame.image.load("d2.png")
    if diceroll==3:
        dice=pygame.image.load("d3.png")
    if diceroll==4:
        dice=pygame.image.load("d4.png")
    if diceroll==5:
        dice=pygame.image.load("d5.png")
    if diceroll==6:
        dice=pygame.image.load("d6.png")
    return (dice,diceroll)

def players():
    msg1=font1.render("Player 1",True,(255,0,0))
    screen.blit(msg1,[60,150])
    msg2=font1.render("Player 2",True,(0,0,255))
    screen.blit(msg2,[60,260])

def rollr():
    msg3=font2.render("Your turn",True,(255,255,255))
    screen.blit(msg3,[60,200])
def rollb():
    msg4=font2.render("Your turn",True,(255,255,255))
    screen.blit(msg4,[60,310])




running=True
#game loop

turn="red"
c=0
d=0

while running:
    screen.fill((0,0,1))


    bck()
    players()

    if turn=="red":
        rollr()
    elif turn=="blue":
        rollb()


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                picknumber()
                dice,diceroll=picknumber()
                screen.blit(dice,(150,60))
                print(diceroll)
            
            if picknumber() and turn=="red":
                turn= "blue"
                if diceroll==6 and rx==30 and ry==150:
                    rx=490
                    ry=500
                    turn="red"
                    c=1
                elif c==1 and ry in [500-i*52 for i in range(0,10,2)]:
                    if rx in range(490,490+(4*52))and diceroll!=6:
                        rx+=(52*diceroll)
                    elif rx in range(490,490+(4*52))and diceroll==6:
                        rx+=(52*diceroll)
                        turn="red"
                    elif rx>=490+(4*52) and diceroll!=6:
                        p=(490+9*52-rx)/52 + 1
                        if (diceroll-p)>=0:
                            rx=490+9*52
                            ry-=52
                            rx-=52*(diceroll-p)
                        else :
                            rx+=52*diceroll
                    elif rx>=490+(4*52) and diceroll==6:
                        p=(490+9*52-rx)/52 + 1
                        if (diceroll-p>=0):
                            rx=490+9*52
                            ry-=52
                            rx-=52*(diceroll-p)
                        else :
                            rx+=52*diceroll
                        turn="red"
                    if rx==490+8*52 and ry==500:
                        rx=490+7*52
                        ry=500-5*52
                    elif rx==490+2*52 and ry==500-52*2:
                        rx=490+52
                        ry=500-5*52
                    elif rx==490+3*52 and ry==500-4*52:
                        rx=490+6*52
                        ry=500-9*52
                    elif rx==490+52 and ry==500-9*52:
                        rx=490+3*52
                        ry=500
                    elif rx==490+7*52 and ry==500-8*52:
                        rx=490+9*52
                        ry=500-3*52
                    elif rx==490+6*52 and ry==500-6*52:
                        rx=490+5*52
                        ry=500
                elif c==1 and ry in [500-i*52 for i in range(1,10,2)]:
                    if rx>=750 and diceroll!=6:
                        rx-=(52*diceroll)
                    elif rx>=750 and diceroll==6:
                        rx-=(52*diceroll)
                        turn="red"
                    elif rx<750 and diceroll!=6 :
                        p=(rx-490)/52 + 1
                        if (diceroll-p)>=0 and ry!=32:
                            rx=490
                            ry-=52
                            rx+=52*(diceroll-p)
                        elif (diceroll-p)<0:
                            rx-=52*diceroll
                        elif (diceroll-p)>=0 and ry==32 : 
                            continue
                    elif rx<750 and diceroll==6 :
                        p=(rx-490)/52 + 1
                        if (diceroll-p)>=0 and ry!=32:
                            rx=490
                            ry-=52
                            rx+=52*(diceroll-p)
                        elif (diceroll-p)<0:
                            rx-=52*diceroll
                        elif (diceroll-p)>=0 and ry==32 : 
                            continue
                        turn="red"
                    if rx==490+8*52 and ry==500:
                        rx=490+7*52
                        ry=500-5*52
                    elif rx==490+2*52 and ry==500-52*2:
                        rx=490+52
                        ry=500-5*52
                    elif rx==490+3*52 and ry==500-4*52:
                        rx=490+6*52
                        ry=500-9*52
                    elif rx==490+52 and ry==500-9*52:
                        rx=490+3*52
                        ry=500
                    elif rx==490+7*52 and ry==500-8*52:
                        rx=490+9*52
                        ry=500-3*52
                    elif rx==490+6*52 and ry==500-6*52:
                        rx=490*5*52
                        ry=500



            elif picknumber() and turn=="blue":
                turn ="red"
                if diceroll==6 and bx==30 and by==260:
                    bx=490
                    by=505
                    turn="blue"
                    d=1
                elif d==1 and by in [505-i*52 for i in range(0,10,2)]:
                    if bx in range(490,490+(4*52))and diceroll!=6:
                        bx+=(52*diceroll)
                    elif bx in range(490,490+(4*52))and diceroll==6:
                        bx+=(52*diceroll)
                        turn="blue"
                    elif bx>=490+(4*52) and diceroll!=6:
                        p=(490+9*52-bx)/52 + 1
                        if (diceroll-p)>=0:
                            bx=490+9*52
                            by-=52
                            bx-=52*(diceroll-p)
                        else :
                            bx+=52*diceroll
                    elif bx>=490+(4*52) and diceroll==6:
                        p=(490+9*52-bx)/52 + 1
                        if (diceroll-p>=0):
                            bx=490+9*52
                            by-=52
                            bx-=52*(diceroll-p)
                        else :
                            bx+=52*diceroll
                        turn="blue"
                    if bx==490+8*52 and by==505:
                        bx=490+7*52
                        by=505-5*52
                    elif bx==490+2*52 and by==505-52*2:
                        bx=490+52
                        by=505-5*52
                    elif bx==490+3*52 and by==505-4*52:
                        bx=490+6*52
                        by=505-9*52
                    elif bx==490+52 and by==505-9*52:
                        bx=490+3*52
                        by=505
                    elif bx==490+7*52 and by==505-8*52:
                        bx=490+9*52
                        by=505-3*52
                    elif bx==490+6*52 and by==505-6*52:
                        bx=490*5*52
                        by=505
                elif d==1 and by in [505-i*52 for i in range(1,10,2)]:
                    if bx>=750 and diceroll!=6:
                        bx-=(52*diceroll)
                    elif bx>=750 and diceroll==6:
                        bx-=(52*diceroll)
                        turn="blue"
                    elif bx<750 and diceroll!=6 :
                        p=(bx-490)/52 + 1
                        if (diceroll-p)>=0 and by!=37:
                            bx=490
                            by-=52
                            bx+=52*(diceroll-p)
                        elif (diceroll-p)<0:
                            bx-=52*diceroll
                        elif (diceroll-p)>=0 and by==37 : 
                            continue
                    elif bx<750 and diceroll==6 :
                        p=(bx-490)/52 + 1
                        if (diceroll-p)>=0 and by!=37:
                            bx=490
                            by-=52
                            bx+=52*(diceroll-p)
                        elif (diceroll-p)<0:
                            bx-=52*diceroll
                        elif (diceroll-p)>=0 and by==37 : 
                            continue
                        turn="blue"
                    if bx==490+8*52 and by==505:
                        bx=490+7*52
                        by=505-5*52
                    elif bx==490+2*52 and by==505-52*2:
                        bx=490+52
                        by=505-5*52
                    elif bx==490+3*52 and by==505-4*52:
                        bx=490+6*52
                        by=505-9*52
                    elif bx==490+52 and by==505-9*52:
                        bx=490+3*52
                        by=505
                    elif bx==490+7*52 and by==505-8*52:
                        bx=490+9*52
                        by=505-3*52
                    elif bx==490+6*52 and by==505-6*52:
                        bx=490*5*52
                        by=505





    
    rplayer(rx,ry)
    bplayer(bx,by)
    pygame.display.update()


    if rx==490 and ry==32:
        screen.fill((0,0,1))
        value=font0.render("RED WON !!!",True,(255,255,102))
        screen.blit(value,[500,300])
        running=False
    if bx==490 and by==37:
        screen.fill((0,0,1))
        value=font0.render("BLUE WON !!!",True,(255,255,102))
        screen.blit(value,[500,300])
        running=False
    time.sleep(1.5)

pygame.display.update()
time.sleep(5)
pygame.quit()
quit()
