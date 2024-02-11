import cv2
import numpy as np
import math
import keyboard as kb
import random
import os

l=[]
x=25
y=25
angle=0
speed=5
c=0
end_angle=0
start_angle=0
pts=0
m=475
n=475
u=475
v=475
g=[1,2]
sp=5

for i in range(25,480,50):
    l.append((25,i))
    l.append((i,25))
    l.append((475,i))
    l.append((i,475))

for i in range(175,430,50):
    l.append((375,i))

l.extend(((175,225),(225,225),(225,275),(175,275),(175,325),(225,325)))

def board(img):
    cv2.rectangle(img,(50,50),(200,200),(0,255,255),-1)
    cv2.rectangle(img,(250,50),(450,150),(0,255,255),-1)
    cv2.rectangle(img,(250,200),(350,300),(0,255,255),-1)
    cv2.rectangle(img,(50,250),(150,450),(0,255,255),-1)
    cv2.rectangle(img,(200,350),(350,450),(0,255,255),-1)
    cv2.rectangle(img,(400,200),(450,450),(0,255,255),-1)

p=random.choice(l)

while True:
    c=c+1
    img=np.full((500,500,3),(0,0,0),dtype=np.uint8)
    board(img)
    cv2.ellipse(img,(x,y),(10,10),angle,start_angle,end_angle,(0,0,255),-1)
    cv2.ellipse(img,p,(5,5),0,0,360,(0,255,0),-1)
    cv2.ellipse(img,(m,n),(10,10),0,0,360,(255,255,255),3)
    cv2.ellipse(img,(u,v),(10,10),0,0,360,(255,255,0),3)
    if (c//20)%2==0:
        start_angle=40
        end_angle=320
    else:
        start_angle=5
        end_angle=355

    if y==25:
        if x==225:
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        elif x==25:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        elif x==475:
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        else:
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
    elif y==175:
        if x==25:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        elif x==225:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
        elif x==375:
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
        elif x==475:
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
        else:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
    elif y==225:
        if x==25:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
        elif x==175:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        elif x==225:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
        elif x==375 or x==475:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        else:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
    elif y==275:
        if x==25:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        elif x==175:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
        elif x==225:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
        elif x==375 or x==475:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        else:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
    elif y==325:
        if x==25:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        elif x==175:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
        elif x==225:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
        elif x==375:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
        elif x==475:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('s'):
                if y<490:
                    y=y+speed
                angle=90
        else:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
    elif y==475:
        if x==25:
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
        elif x==175 or x==375:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
        elif x==475:
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
            if kb.is_pressed('w'):
                if y>10:
                    y=y-speed
                angle=270
        else:
            if kb.is_pressed('d'):
                if x<490:
                    x=x+speed
                angle=0
            if kb.is_pressed('a'):
                if x>10:
                    x=x-speed
                angle=180
    else:
        if kb.is_pressed('w'):
            if y>10:
                y=y-speed
            angle=270
        if kb.is_pressed('s'):
            if y<490:
                y=y+speed
            angle=90
    
    d=math.sqrt((x-p[0])*(x-p[0])+(y-p[1])*(y-p[1]))
    if d<=15:
        p=random.choice(l)
        pts=pts+1
    if m==475 and n==475:
        f=1
        k=0
    elif m==475 and n==175:
        f=2
        k=0
    elif m==475 and n==25:
        f=3
        k=0
    elif m==375 and n==475:
        f=4
        k=0
    elif m==175 and n==475:
        f=5
        k=0
    elif m==25 and n==475:
        f=6
        k=0
    elif m==25 and n==225:
        f=7
        k=0
    elif m==225 and n==25:
        f=8
        k=0
    elif m==25 and n==25:
        f=9
        k=0
    elif m==225 and n==225:
        f=10
        k=0
    elif m==225 and n==325:
        f=11
        k=0
    elif m==175 and n==325:
        f=12
        k=0
    elif m==375 and n==325:
        f=13
        k=0
    elif m==175 and n==225:
        f=14
        k=0
    elif m==375 and n==175:
        f=15
        k=0
    elif m==225 and n==175:
        f=16
        k=0
    else:
        f=f+1
        f=f-1
    if f==1:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n-sp
        else:
            m=m-sp
    elif f==2:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n-sp
        else:
            m=m-sp
    elif f==3:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m-sp
    elif f==4:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n-sp
        else:
            m=m-sp
    elif f==5:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n-sp
        else:
            m=m-sp
    elif f==6:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n-sp
        else:
            m=m+sp
    elif f==7:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n-sp
        else:
            m=m+sp
    elif f==8:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m-sp
    elif f==9:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m+sp
    elif f==10:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            n=n-sp
    elif f==11:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            m=m+sp
        else:
            n=n-sp
    elif f==12:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m+sp
    elif f==13:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m-sp
    elif f==14:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m+sp
    elif f==15:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            n=n+sp
        else:
            m=m-sp
    elif f==16:
        if k==0:
            ch=random.choice(g)
        k=1
        if ch==1:
            m=m+sp
        else:
            n=n+sp
    else:
        f=f+1
        f=f-1
    if u==475 and v==475:
        s=1
        k2=0
    elif u==475 and v==175:
        s=2
        k2=0
    elif u==475 and v==25:
        s=3
        k2=0
    elif u==375 and v==475:
        s=4
        k2=0
    elif u==175 and v==475:
        s=5
        k2=0
    elif u==25 and v==475:
        s=6
        k2=0
    elif u==25 and v==225:
        s=7
        k2=0
    elif u==225 and v==25:
        s=8
        k2=0
    elif u==25 and v==25:
        s=9
        k2=0
    elif u==225 and v==225:
        s=10
        k2=0
    elif u==225 and v==325:
        s=11
        k2=0
    elif u==175 and v==325:
        s=12
        k2=0
    elif u==375 and v==325:
        s=13
        k2=0
    elif u==175 and v==225:
        s=14
        k2=0
    elif u==375 and v==175:
        f=15
        k2=0
    elif u==225 and v==175:
        s=16
        k2=0
    else:
        s=s+1
        s=s-1
    if s==1:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v-sp
        else:
            u=u-sp
    elif s==2:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v-sp
        else:
            u=u-sp
    elif s==3:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u-sp
    elif s==4:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v-sp
        else:
            u=u-sp
    elif s==5:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v-sp
        else:
            u=u-sp
    elif s==6:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v-sp
        else:
            u=u+sp
    elif s==7:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u+sp
    elif s==8:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u-sp
    elif s==9:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u+sp
    elif s==10:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            v=v-sp
    elif s==11:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            u=u+sp
        else:
            v=v-sp
    elif s==12:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u+sp
    elif s==13:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u-sp
    elif s==14:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u+sp
    elif s==15:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            v=v+sp
        else:
            u=u-sp
    elif s==16:
        if k2==0:
            choic=random.choice(g)
        k2=1
        if choic==1:
            u=u+sp
        else:
            v=v+sp
    else:
        s=s+1
        s=s-1
    d2=math.sqrt((x-m)*(x-m)+(y-n)*(y-n))
    d3=math.sqrt((x-u)*(x-u)+(y-v)*(y-v))
    if d2<10 or d3<10:
        message = "GAME OVER"
        font_size = 2
        font_color = (0, 0, 255)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, baseline = cv2.getTextSize(message, font, font_size, 2)
        text_center_x = int((img.shape[1] - text_size[0]) / 2)
        text_center_y = int((img.shape[0] + text_size[1]) / 2)
        cv2.putText(img, message, (text_center_x, text_center_y - baseline), font, font_size, font_color, 2)
        cv2.imshow("pac",img)
        cv2.waitKey(3000)
        message = "SCORE:"+str(pts)
        font_size = 2
        font_color = (0, 0, 255)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, baseline = cv2.getTextSize(message, font, font_size, 2)
        text_center_x = int((img.shape[1] - text_size[0]) / 2)
        text_center_y = int((img.shape[0] + text_size[1]) / 2)
        cv2.putText(img, message, (text_center_x, text_center_y - baseline), font, font_size, font_color, 2)
        cv2.imshow("pac",img)
        cv2.waitKey(3000)
        os._exit(0)
    cv2.imshow("hehe",img)
    if cv2.waitKey(10)==ord("q"):
        break
cv2.destroyAllWindows()