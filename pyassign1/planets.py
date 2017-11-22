import turtle
import math

wn=turtle.Screen()
wn.screensize(1000,1000)

sun=turtle.Turtle()
sun.color("yellow")
sun.shape("circle")
sun.shapesize(2)

t=["mercury","venus","earth","mars","jupiter","saturn"]
a=[40,70,100,140,190,250]
b=[40,65,90,120,160,200]
m=["blue","green","red","black","orange","light blue"]
n=[0.5,0.5,0.5,0.5,1,1]
r=[1,2,3,4,5,6]

for p in range(6):
    t[p]=turtle.Turtle()
    t[p].shape("circle")
    t[p].shapesize(n[p])
    t[p].color(m[p])

def put(t,a,b):
    c=math.sqrt(a*a-b*b)
    t.up()
    t.goto(a-c,0)
    t.down()

def move(t,a,b,r):
    c=math.sqrt(a*a-b*b)
    x=a*math.cos(l/(2*math.pi*r))-c
    y=b*math.sin(l/(2*math.pi*r))
    t.goto(x,y)

for p in range(6):
    put(t[p],a[p],b[p])

for i in range(600000):
    k=i%6
    l=i//6
    move(t[k],a[k],b[k],r[k])

turtle.mainloop()
