from tkinter import *
def point(x,y):
    canvas.create_oval(x-5, y-5, x+5, y+5, width=0, fill='blue')
def point2(x,y):
    canvas.create_oval(x-10, y-10, x+10, y+10, width=0, fill='red')
canvas = Canvas(width=800, height=800, bg='white')
canvas.pack(expand=YES, fill=BOTH)


class DOT:
    def __init__(self,x,y):
        self.x=x
        self.y=y    
    def getx(self):
        return self.x
    def gety(self):
        return self.y
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
    def ktoend(self,end,k):
        return DOT((end.x-self.x)*k+self.x,(end.y-self.y)*k+self.y)  

def gettempdot(lst):
    result=[]
    for i in range(len(lst)-2):
        zd1=(lst[i+1]+lst[i])/2
        zd2=(lst[i+2]+lst[i+1])/2
        j=(lst[i+1]%lst[i])/(lst[i+2]%lst[i+1])
        k=j/(j+1)
        Es=zd1.ktoend(zd2,k)
        R1=lst[i+1]-(Es-zd1)
        R2=lst[i+1]+(zd2-Es)
        result.append(R1)
        result.append(R2)
    return result



def Bsal4(A,B,num,R1,R2):
    result=[]
    for i in range(num+2):
        t=(1/(num+1))*i
        tempdot=A*((1-t)**3)+R1*3*t*(1-t)*(1-t)+R2*3*t*t*(1-t)+B*t*t*t
        result.append(tempdot)
    return result

def show(lst,num):
    a=lst
    b=gettempdot(lst)
    alldot=[]
    for i in range(len(lst)-1):
        if (i==0):
            alldot += Bsal4(lst[0],lst[1],num,b[0],b[0])
        elif (i==len(lst)-2):
            alldot += Bsal4(lst[len(lst)-2],lst[len(lst)-1],num,b[len(b)-1],b[len(b)-1])
        else:
            alldot += Bsal4(lst[i],lst[i+1],num,b[2*i-1],b[2*i])
    return alldot


dotslst=[]
def refr(e):
    global dotslst
    dotslst.append(DOT(e.x,e.y))
    canvas.delete(ALL)
    for i in dotslst:
        point2(i.x,i.y)
    for i in show(dotslst,500):
        point(i.x,i.y)

def clea(e):
    global dotslst
    dotslst=[]
    canvas.delete(ALL)
 
canvas.bind("<Button-1>",func=refr)
canvas.bind("<Button-3>",func=clea)



mainloop()
