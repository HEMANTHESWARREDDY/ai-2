import time
x=0
y=0
intialstate=[0,0]
goal=[int(i) for i in input("ENTER YOUR GOAL  ").split(" ")]
xmax=int(input("ENTER THE MAX LIMIT OF X  "))
ymax=int(input("ENTER THE MAX LIMIT OF Y  "))
time.sleep(3)
if x==0 and y==0:
    print("i am filling Y jug with 3 gaalons of water through pump")
    y+=ymax
    print([x,y])
    time.sleep(3)
    print("now Y=",y)
    x=y
    time.sleep(3)
    print("filling X jug  with the help of Y now X=",x)
    y=0
    print([x,y])
    if y==0:
        time.sleep(3)
        print("filling Y jug again with 3 gaalons of water")
        y+=ymax
        time.sleep(3)
        print("now Y=",y)
        
        print([x,y])
        for i in range(xmax):
            if x<xmax:
                x+=1
                y-=1
            elif x==xmax:
                time.sleep(3)
                print("X is max now",x)
                time.sleep(3)
                print([x,y])
                time.sleep(3)
                print("we are pouring down the water which are in X on ground")
                x-=xmax
                time.sleep(3)
                print([x,y])
                time.sleep(3)
                print("pouring the "+str(y)+"gaalons of water into X from Y")
                x+=y
                y=0
                break
z=[x,y]
print(z)
if z==goal:
    time.sleep(3)
    print("GIVEN TASK IS COMPLETED SUCCESSFULLY")
    time.sleep(3)
    print("FINAL OUTPUT=",z)