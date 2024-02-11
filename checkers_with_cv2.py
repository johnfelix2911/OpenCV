import cv2
import numpy as np
import keyboard as kb

def green(x,y,img):
    cv2.ellipse(img,(x,y),(45,45),0,0,360,(0,255,0),-1)

def red(x,y,img):
    cv2.ellipse(img,(x,y),(45,45),0,0,360,(0,0,255),-1)

def board():
    while True:
        cv2.imshow("checkers",img)
        if cv2.waitKey(10)==ord("q"):
            break
    
def play(p,r,):
    while True:
        col=int(input("enter the column: "))
        row=int(input("enter the row: "))
        if row==1:
            if a[col-1]==" " and col<=5:
                a[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==2:
            if b[col-1]==" " and col<=5:
                b[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==3:
            if c[col-1]==" " and col<=5:
                c[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==4:
            if d[col-1]==" " and col<=5:
                d[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==5:
            if e[col-1]==" " and col<=5:
                e[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        else:
            print("row is out of limits")
    if row==1:
        if col==1:
            if a[1]==r and a[2]==p:
                a[1]=p
            if a[1]==r and a[2]==r and a[3]==p:
                a[1]=p
                a[2]=p
            if a[1]==r and a[2]==r and a[3]==r and a[4]==p:
                a[1]=p
                a[2]=p
                a[3]=p
            if b[0]==r and c[0]==p:
                b[0]=p
            if b[0]==r and c[0]==r and d[0]==p:
                b[0]=p
                c[0]=p
            if b[0]==r and c[0]==r and d[0]==r and e[0]==p:
                b[0]=p
                c[0]=p
                d[0]=p
            if b[1]==r and c[2]==p:
                b[1]=p
            if b[1]==r and c[2]==r and d[3]==p:
                b[1]=p
                c[2]=p
            if b[1]==r and c[2]==r and d[3]==r and e[4]==p:
                b[1]=p
                c[2]=p
                d[3]=p
        if col==2:
            if a[2]==r and a[3]==p:
                a[2]=p
            if a[2]==r and a[3]==r and a[4]==p:
                a[2]=p
                a[3]=p
            if b[1]==r and c[1]==p:
                b[1]=p
            if b[1]==r and c[1]==r and d[1]==p:
                b[1]=p
                c[1]=p
            if b[1]==r and c[1]==r and d[1]==r and e[1]==p:
                b[1]=p
                c[1]=p
                d[1]=p
            if b[2]==r and c[3]==p:
                b[2]=p
            if b[2]==r and c[3]==r and d[4]==p:
                b[2]=p
                c[3]=p
        if col==3:
            if a[1]==r and a[0]==p:
                a[1]=p
            if a[3]==r and a[4]==p:
                a[3]=p
            if b[1]==r and c[0]==p:
                b[1]=p
            if b[3]==r and c[4]==p:
                b[3]=p
            if b[2]==r and c[2]==p:
                b[2]=p
            if b[2]==r and c[2]==r and d[2]==p:
                b[2]=p
                c[2]=p
            if b[2]==r and c[2]==r and d[2]==r and e[2]==p:
                b[2]=p
                c[2]=p
                d[2]=p
        if col==4:
            if a[2]==r and a[1]==p:
                a[2]=p
            if a[2]==r and a[1]==r and a[0]==p:
                a[2]=p
                a[1]=p
            if b[3]==r and c[3]==p:
                b[3]=p
            if b[3]==r and c[3]==r and d[3]==p:
                b[3]=p
                c[3]=p
            if b[3]==r and c[3]==r and d[3]==r and e[3]==p:
                b[3]=p
                c[3]=p
                d[3]=p
            if b[2]==r and c[1]==p:
                b[2]=p
            if b[2]==r and c[1]==r and d[0]==p:
                b[2]=p
                c[1]=p
        if col==5:
            if a[3]==r and a[2]==p:
                a[3]=p
            if a[3]==r and a[2]==r and a[1]==p:
                a[3]=p
                a[2]=p
            if a[3]==r and a[2]==r and a[1]==r and a[0]==p:
                a[3]=p
                a[2]=p
                a[1]=p
            if b[4]==r and c[4]==p:
                b[4]=p
            if b[4]==r and c[4]==r and d[4]==p:
                b[4]=p
                c[4]=p
            if b[4]==r and c[4]==r and d[4]==r and e[4]==p:
                b[4]=p
                c[4]=p
                d[4]=p
            if b[3]==r and c[2]==p:
                b[3]=p
            if b[3]==r and c[2]==r and d[1]==p:
                b[3]=p
                c[2]=p
            if b[3]==r and c[2]==r and d[1]==r and e[0]==p:
                b[3]=p
                c[2]=p
                d[1]=p
    if row==2:
        if col==1:
            if b[1]==r and b[2]==p:
                b[1]=p
            if b[1]==r and b[2]==r and b[3]==p:
                b[1]=p
                b[2]=p
            if b[1]==r and b[2]==r and b[3]==r and b[4]==p:
                b[1]=p
                b[2]=p
                b[3]=p
            if c[0]==r and d[0]==p:
                c[0]=p
            if c[0]==r and d[0]==r and e[0]==p:
                c[0]=p
                d[0]=p
            if c[1]==r and d[2]==p:
                c[1]=p
            if c[1]==r and d[2]==r and e[3]==p:
                c[1]=p
                d[2]=p
        if col==2:
            if b[2]==r and b[3]==p:
                b[2]=p
            if b[2]==r and b[3]==r and b[4]==p:
                b[2]=p
                b[3]=p
            if c[1]==r and d[1]==p:
                c[1]=p
            if c[1]==r and d[1]==r and e[1]==p:
                c[1]=p
                d[1]=p
            if c[2]==r and d[3]==p:
                c[2]=p
            if c[2]==r and d[3]==r and e[4]==p:
                c[2]=p
                d[3]=p
        if col==3:
            if b[1]==r and b[0]==p:
                b[1]=p
            if b[3]==r and b[4]==p:
                b[3]=p
            if c[2]==r and d[2]==p:
                c[2]=p
            if c[2]==r and d[2]==r and e[2]==p:
                c[2]=p
                d[2]=p
        if col==4:
            if b[2]==r and b[1]==p:
                b[2]=p
            if b[2]==r and b[1]==r and b[0]==p:
                b[2]=p
                b[1]=p
            if c[3]==r and d[3]==p:
                c[3]=p
            if c[3]==r and d[3]==r and e[3]==p:
                c[3]=p
                d[3]=p
            if c[2]==r and d[1]==p:
                c[2]=p
            if c[2]==r and d[1]==r and e[0]==p:
                c[2]=p
                d[3]=p
        if col==5:
            if b[3]==r and b[2]==p:
                b[3]=p
            if b[3]==r and b[2]==r and b[1]==p:
                b[3]=p
                b[2]=p
            if b[3]==r and b[2]==r and b[1]==r and b[0]==p:
                b[3]=p
                b[2]=p
                b[1]=p
            if c[3]==r and d[2]==p:
                c[3]=p
            if c[3]==r and d[2]==r and e[1]==p:
                c[3]=p
                d[2]=p
            if c[4]==r and d[4]==p:
                c[4]=p
            if c[4]==r and d[4]==r and e[4]==p:
                c[4]=p
                d[4]=p
    if row==3:
        if col==1:
            if c[1]==r and c[2]==p:
                c[1]=p
            if c[1]==r and c[2]==r and c[3]==p:
                c[1]=p
                c[2]=p
            if c[1]==r and c[2]==r and c[3]==r and c[4]==p:
                c[1]=p
                c[2]=p
                c[3]=p
            if b[0]==r and a[0]==p:
                b[0]=p
            if d[0]==r and e[0]==p:
                d[0]=p
            if b[1]==r and a[2]==p:
                b[1]=p
            if d[1]==r and e[2]==p:
                d[1]=p
        if col==2:
            if c[2]==r and c[3]==p:
                c[2]=p
            if c[2]==r and c[3]==r and c[4]==p:
                c[2]=p
                c[3]=p
            if b[1]==r and a[1]==p:
                b[1]=p
            if d[1]==r and e[1]==p:
                d[1]=p
        if col==3:
            if b[2]==r and a[2]==p:
                b[2]=p
            if c[3]==r and c[4]==p:
                c[3]=p
            if c[1]==r and c[0]==p:
                c[1]=p
            if d[2]==r and e[2]==p:
                d[2]=p
            if b[1]==r and a[0]==p:
                b[1]=p
            if b[3]==r and a[4]==p:
                b[3]=p
            if d[1]==r and e[0]==p:
                d[1]=p
            if d[3]==r and e[4]==p:
                d[3]=p
        if col==4:
            if c[2]==r and c[1]==p:
                c[2]=p
            if c[2]==r and c[1]==r and c[0]==p:
                c[2]=p
                c[1]=p
            if b[3]==r and a[3]==p:
                b[3]=p
            if d[3]==r and e[3]==p:
                d[3]=p
        if col==5:
            if b[4]==r and a[4]==p:
                b[4]=p
            if d[4]==r and e[4]==p:
                d[4]=p
            if c[3]==r and c[2]==p:
                c[3]=p
            if c[3]==r and c[2]==r and c[1]==p:
                c[3]=p
                c[2]=p
            if c[3]==r and c[2]==r and c[1]==r and c[0]==p:
                c[3]=p
                c[2]=p
                c[1]=p
            if b[3]==r and a[2]==p:
                b[3]=p
            if d[3]==r and e[2]==p:
                d[3]=p
    if row==4:
        if col==1:
            if d[1]==r and d[2]==p:
                d[1]=p
            if d[1]==r and d[2]==r and d[3]==p:
                d[1]=p
                d[2]=p
            if d[1]==r and d[2]==r and d[3]==r and d[4]==p:
                d[1]=p
                d[2]=p
                d[3]=p
            if c[0]==r and b[0]==p:
                c[0]=p
            if c[0]==r and b[0]==r and a[0]==p:
                c[0]=p
                b[0]=p
            if c[1]==r and b[2]==p:
                c[1]=p
            if c[1]==r and b[2]==r and a[3]==p:
                c[1]=p
                b[2]=p
        if col==2:
            if d[2]==r and d[3]==p:
                d[2]=p
            if d[2]==r and d[3]==r and d[4]==p:
                d[2]=p
                d[3]=p
            if c[1]==r and b[1]==p:
                c[1]=p
            if c[1]==r and b[1]==r and a[1]==p:
                c[1]=p
                b[1]=p
            if c[2]==r and b[3]==p:
                c[2]=p
            if c[2]==r and b[3]==r and a[4]==p:
                c[2]=p
                b[3]=p
        if col==3:
            if d[1]==r and d[0]==p:
                d[1]=p
            if d[3]==r and d[4]==p:
                d[3]=p
            if c[2]==r and b[2]==p:
                c[2]=p
            if c[2]==r and b[2]==r and a[2]==p:
                c[2]=p
                b[2]=p
        if col==4:
            if d[2]==r and d[1]==p:
                d[2]=p
            if d[2]==r and d[1]==r and d[0]==p:
                d[2]=p
                d[1]=p
            if c[3]==r and b[3]==p:
                c[3]=p
            if c[3]==r and b[3]==r and a[3]==p:
                c[3]=p
                b[3]=p
            if c[2]==r and b[1]==p:
                c[2]=p
            if c[2]==r and b[1]==r and a[0]==p:
                c[2]=p
                b[3]=p
        if col==5:
            if d[3]==r and d[2]==p:
                d[3]=p
            if d[3]==r and d[2]==r and d[1]==p:
                d[3]=p
                d[2]=p
            if d[3]==r and d[2]==r and d[1]==r and d[0]==p:
                d[3]=p
                d[2]=p
                d[1]=p
            if c[3]==r and b[2]==p:
                c[3]=p
            if c[3]==r and b[2]==r and a[1]==p:
                c[3]=p
                b[2]=p
            if c[4]==r and b[4]==p:
                c[4]=p
            if c[4]==r and b[4]==r and a[4]==p:
                c[4]=p
                b[4]=p
    if row==5:
        if col==1:
            if e[1]==r and e[2]==p:
                e[1]=p
            if e[1]==r and e[2]==r and e[3]==p:
                e[1]=p
                e[2]=p
            if e[1]==r and e[2]==r and e[3]==r and e[4]==p:
                e[1]=p
                e[2]=p
                e[3]=p
            if d[0]==r and c[0]==p:
                d[0]=p
            if d[0]==r and c[0]==r and b[0]==p:
                d[0]=p
                c[0]=p
            if d[0]==r and c[0]==r and b[0]==r and a[0]==p:
                d[0]=p
                c[0]=p
                b[0]=p
            if d[1]==r and c[2]==p:
                d[1]=p
            if d[1]==r and c[2]==r and b[3]==p:
                d[1]=p
                c[2]=p
            if d[1]==r and c[2]==r and b[3]==r and a[4]==p:
                b[1]=p
                c[2]=p
                d[3]=p
        if col==2:
            if e[2]==r and e[3]==p:
                e[2]=p
            if e[2]==r and e[3]==r and e[4]==p:
                e[2]=p
                e[3]=p
            if d[1]==r and c[1]==p:
                d[1]=p
            if d[1]==r and c[1]==r and b[1]==p:
                d[1]=p
                c[1]=p
            if d[1]==r and c[1]==r and b[1]==r and a[1]==p:
                d[1]=p
                c[1]=p
                b[1]=p
            if d[2]==r and c[3]==p:
                d[2]=p
            if d[2]==r and c[3]==r and b[4]==p:
                d[2]=p
                c[3]=p
        if col==3:
            if e[1]==r and e[0]==p:
                e[1]=p
            if e[3]==r and e[4]==p:
                e[3]=p
            if d[1]==r and c[0]==p:
                d[1]=p
            if d[3]==r and c[4]==p:
                d[3]=p
            if d[2]==r and c[2]==p:
                d[2]=p
            if d[2]==r and c[2]==r and b[2]==p:
                d[2]=p
                c[2]=p
            if d[2]==r and c[2]==r and b[2]==r and a[2]==p:
                b[2]=p
                c[2]=p
                d[2]=p
        if col==4:
            if e[2]==r and e[1]==p:
                e[2]=p
            if e[2]==r and e[1]==r and e[0]==p:
                e[2]=p
                e[1]=p
            if d[3]==r and c[3]==p:
                d[3]=p
            if d[3]==r and c[3]==r and b[3]==p:
                d[3]=p
                c[3]=p
            if d[3]==r and c[3]==r and b[3]==r and a[3]==p:
                d[3]=p
                c[3]=p
                b[3]=p
            if d[2]==r and c[1]==p:
                d[2]=p
            if d[2]==r and c[1]==r and b[0]==p:
                d[2]=p
                c[1]=p
        if col==5:
            if e[3]==r and e[2]==p:
                e[3]=p
            if e[3]==r and e[2]==r and e[1]==p:
                e[3]=p
                e[2]=p
            if e[3]==r and e[2]==r and e[1]==r and e[0]==p:
                e[3]=p
                e[2]=p
                e[1]=p
            if d[4]==r and c[4]==p:
                d[4]=p
            if d[4]==r and c[4]==r and b[4]==p:
                d[4]=p
                c[4]=p
            if d[4]==r and c[4]==r and b[4]==r and a[4]==p:
                b[4]=p
                c[4]=p
                d[4]=p
            if d[3]==r and c[2]==p:
                d[3]=p
            if d[3]==r and c[2]==r and b[1]==p:
                d[3]=p
                c[2]=p
            if d[3]==r and c[2]==r and b[1]==r and a[0]==p:
                d[3]=p
                c[2]=p
                b[1]=p

def convert(l,y):
    for i in range(len(l)):
        if l[i]=="x":
            x=100*i+50
            red(x,y,img)
        elif l[i]=="o":
            x=100*i+50
            green(x,y,img)
        else:
            continue

def read():
    print("Enter column")
    col=kb.read_key()
    print("Enter row")
    row=kb.read_key()
        
img=np.full((500,500,3),(0,0,0),dtype=np.uint8)

cv2.line(img,(100,0),(100,500),(0,255,255),2)
cv2.line(img,(200,0),(200,500),(0,255,255),2)
cv2.line(img,(300,0),(300,500),(0,255,255),2)
cv2.line(img,(400,0),(400,500),(0,255,255),2)

cv2.line(img,(0,100),(500,100),(0,255,255),2)
cv2.line(img,(0,200),(500,200),(0,255,255),2)
cv2.line(img,(0,300),(500,300),(0,255,255),2)
cv2.line(img,(0,400),(500,400),(0,255,255),2)

cv2.imshow("checkers",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

a=[" "," "," "," "," "]
b=[" "," "," "," "," "]
c=[" "," "," "," "," "]
d=[" "," "," "," "," "]
e=[" "," "," "," "," "]

z=0
for i in range(25):
    if z%2==0:
        play("x","o")
        convert(a,50)
        convert(b,150)
        convert(c,250)
        convert(d,350)
        convert(e,450)
        board()
        z=z+1
    else:
        play("o","x")
        convert(a,50)
        convert(b,150)
        convert(c,250)
        convert(d,350)
        convert(e,450)
        board()
        z=z+1