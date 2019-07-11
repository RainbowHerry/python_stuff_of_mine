from math import *
from tkinter import *
canvas = Canvas(width=800, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)
class DOT:
    def __init__(self,x,y):
        self.x=x
        self.y=y    
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getm(self):
        return (self.x**2+self.y**2)**0.5
    def __add__(self,b):
        return DOT(self.x+b.x,self.y+b.y)
    def __sub__(self,b):
        return DOT(self.x-b.x,self.y-b.y)
    def __mul__(self,b):
        return DOT(self.x*b,self.y*b)
    def __truediv__(self,b):
        return DOT(self.x/b,self.y/b)
    def __mod__(self,b):
        return ((self.x-b.x)**2+(self.y-b.y)**2)**0.5
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def ktoend(self,end,k):
        return DOT((end.x-self.x)*k+self.x,(end.y-self.y)*k+self.y)

def turnandgo(V1,Deg,Leng,A):
    R=Deg/180*pi
    eV1=V1/V1.getm()
    V1p=DOT(eV1.x*cos(R)-eV1.y*sin(R),eV1.x*sin(R)+eV1.y*cos(R))*Leng
    return A+V1p

def doonce(lst,method):
    result=[]
    for i in range(len(lst)-1):
        tempr=[]
        tempr.append(lst[i])
        l=lst[i+1]%lst[i]
        V1=lst[i+1]-lst[i]
        A=lst[i]
        for j in method:
            r1=turnandgo(V1,j[0],l*j[1],A)
            tempr.append(r1)
            V1=r1-A
            A=r1
        result.append(tempr)
    return result
      
def doall(lst,method,times):
    result=[]
    if(times==0):
        return lst
    else:
        for k in doall(lst,method,times-1):
            result += doonce(k,method)
        return result

def line(L):
    ll=[]
    for i in L:
        ll.append(i.x)
        ll.append(i.y)
    canvas.create_line(ll)
#初始起点和终点
S=[[DOT(200,200),DOT(600,200)]]
S2=[[DOT(390,300),DOT(410,300)]]
#变形方法，这里为左转45°，向前走根号0.5，再向右转90°,向前走根号0.5
method=[[45,(2**0.5)/2],[0-90,(2**0.5)/2]]
method2=[[0,1/3],[60,1/3],[-120,1/3],[60,1/3]]
method3=[[0,0.5],[90,0.25],[-180,0.25],[90,0.5]]
#
for i in doall(S,method3,8):
    line(i)


mainloop()
        



    
    
