####遥感作业
import copy
class Table:
    def __init__(self,strs=""):
        self.strs=strs
        self.big=[]
        self.table=[]
        self.splitme()
        self.evalme()
        self.bighim()

    def __str__(self): 
        res=""
        m=self.maxofme()
        for j in self.table:
            for k in j:
                res+=" "*(m-len(str(k)))+str(k)+" "
            res=res[:-1]+"\n"
        return res
    
    def get_size(self):
        return (len(self.table[0]),len(self.table))

    def get_str(self):
        res=""
        for j in self.table:
            for k in j:
                res+=str(k)+","
            res=res[:-1]+"\n"
        return res[:-1]

    def maxofme(self):
        res=0
        for j in self.table:
            for k in j:
                if(res<len(str(k))):
                    res=len(str(k))
        return res
    
    def splitme(self):
        hang=self.strs.split("\n")
        for i in hang:
            if(True):
                self.table.append(i.split(","))

    def evalme(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                try:
                    self.table[i][j]=eval(self.table[i][j])
                except:
                    pass

    def roundme(self,n):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                self.table[i][j]=round(self.table[i][j],n)
    
    def strme(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                self.table[i][j]=str(self.table[i][j])
                
    def bighim(self):
        self.big.append([self.table[0][0]]+self.table[0]+[self.table[0][-1]])
        for i in range(len(self.table)):
            self.big.append([self.table[i][0]]+self.table[i]+[self.table[i][-1]])
        self.big.append([self.table[-1][0]]+self.table[-1]+[self.table[-1][-1]])

    def f(self,pat):
        if (type(pat)!=type(self)):
            raise RuntimeError("模板类型错误！")
        else:
            self.bighim()
            res=Table("")
            res.table=copy.deepcopy(self.table)
            if(pat.strs=="中值滤波"):
                for i in range(len(self.table)):
                    for j in range(len(self.table[i])):
                        tempdata=[self.big[i][j],self.big[i][j+1],self.big[i][j+2],\
                                  self.big[i+1][j],self.big[i+1][j+1],self.big[i+1][j+2],\
                                  self.big[i+2][j],self.big[i+2][j+1],self.big[i+2][j+2],]
                        tempdata.sort()
                        res.table[i][j]=tempdata[4]
            elif(pat.get_size()==(3,3)):
                for i in range(len(self.table)):
                    for j in range(len(self.table[i])):
                        res.table[i][j]=self.big[i][j]*pat.table[0][0]+\
                        self.big[i][j+1]*pat.table[0][1]+\
                        self.big[i][j+2]*pat.table[0][2]+\
                        self.big[i+1][j]*pat.table[1][0]+\
                        self.big[i+1][j+1]*pat.table[1][1]+\
                        self.big[i+1][j+2]*pat.table[1][2]+\
                        self.big[i+2][j]*pat.table[2][0]+\
                        self.big[i+2][j+1]*pat.table[2][1]+\
                        self.big[i+2][j+2]*pat.table[2][2]
            elif(pat.strs=="索伯尔梯度"):
                for i in range(len(self.table)):
                    for j in range(len(self.table[i])):
                        pat1=Table("1,2,1\n0,0,0\n-1,-2,-1")
                        pat2=Table("-1,0,1\n-2,0,2\n-1,0,1")
                        res.table[i][j]=abs(self.big[i][j]*pat1.table[0][0]+\
                        self.big[i][j+1]*pat1.table[0][1]+\
                        self.big[i][j+2]*pat1.table[0][2]+\
                        self.big[i+1][j]*pat1.table[1][0]+\
                        self.big[i+1][j+1]*pat1.table[1][1]+\
                        self.big[i+1][j+2]*pat1.table[1][2]+\
                        self.big[i+2][j]*pat1.table[2][0]+\
                        self.big[i+2][j+1]*pat1.table[2][1]+\
                        self.big[i+2][j+2]*pat1.table[2][2])
                        res.table[i][j]+=abs(self.big[i][j]*pat2.table[0][0]+\
                        self.big[i][j+1]*pat2.table[0][1]+\
                        self.big[i][j+2]*pat2.table[0][2]+\
                        self.big[i+1][j]*pat2.table[1][0]+\
                        self.big[i+1][j+1]*pat2.table[1][1]+\
                        self.big[i+1][j+2]*pat2.table[1][2]+\
                        self.big[i+2][j]*pat2.table[2][0]+\
                        self.big[i+2][j+1]*pat2.table[2][1]+\
                        self.big[i+2][j+2]*pat2.table[2][2])
            elif(pat.strs=="罗伯特梯度"):
                for i in range(len(self.table)):
                    for j in range(len(self.table[i])):
                        res.table[i][j]=abs(self.big[i+1][j+1]*-1+\
                        self.big[i+2][j+2]*1)+abs(self.big[i+1][j+2]*1+\
                        self.big[i+2][j+1]*-1)
            elif(pat.get_size()==(2,2)):
                for i in range(len(self.table)):
                    for j in range(len(self.table[i])):
                        res.table[i][j]=(self.big[i+1][j+1]*pat.table[0][0]+\
                        self.big[i+2][j+2]*pat.table[1][1])+(self.big[i+1][j+2]*pat.table[0][1]+\
                        self.big[i+2][j+1]*pat.table[1][0])
                        
            else:
                return("暂不支持该模板！\n请输入3x3或者2x2矩阵或者'中值滤波'、'罗伯特梯度'、'索伯尔梯度'！")

            res.roundme(2)#2表示小数点位数
            res.strme()
            return(res)
    
        
###使用方法：######################################

A="""4,3,7,6,8
2,15,8,9,9
5,8,9,13,10
7,9,12,15,11
8,11,10,14,13"""

PAT1="""1/9,1/9,1/9
1/9,1/9,1/9
1/9,1/9,1/9"""

PAT2="中值滤波"

###print(Table.f(Table(输入矩阵),Table(模板)))
print(Table.f(Table(A),Table(PAT1)))
print(Table.f(Table(A),Table(PAT2)))
####################################################

#以下为GUI
from tkinter import *
rt=Tk()
rt.title("遥感作业计算程序")
results=""
rt.geometry("450x150+"+str(int(rt.winfo_screenwidth()/2-225))+"+"+str(int(rt.winfo_screenheight()/2-75)))
def b1f():
    global e3,results
    e3.delete('0.0','end')
    results=Table.f(Table(e1.get("0.0","end")[:-1]),Table(e2.get("0.0","end")[:-1]))
    e3.insert(INSERT,results)
def b2f():
    global e3,results
    e1.delete('0.0','end')
    e1.insert(INSERT,results.get_str())

s1=A
s2=PAT1
s3=""
e1=Text()
e2=Text()
e3=Text()
e1.insert(INSERT,s1)
e2.insert(INSERT,s2)
e3.insert(INSERT,"模板为3x3或者2x2的矩阵或者算法名称(例如罗伯特梯度、索伯尔梯度、中值滤波)。\n半角逗号连接，回车换行。")
l1=Label(text="输入矩阵：")
l2=Label(text="模板：")
b1=Button(text="计算",command=b1f)
b2=Button(text="结果转输入",command=b2f)
rt.rowconfigure(0,weight=1,minsize=20)
rt.rowconfigure(1,weight=4,minsize=80)
rt.columnconfigure(0,weight=1,minsize=30)
rt.columnconfigure(1,weight=1,minsize=15)
rt.columnconfigure(2,weight=1,minsize=110)
rt.columnconfigure(3,weight=1,minsize=110)
l1.grid(column=0,row=0,stick=W+N+S+E)
e1.grid(column=0,row=1,stick=W+N+S+E)
l2.grid(column=1,row=0,stick=W+N+S+E)
e2.grid(column=1,row=1,stick=W+N+S+E)
b1.grid(column=3,row=0,stick=N+S)
b2.grid(column=2,row=0,stick=N+S)
e3.grid(column=2,row=1,columnspan=2,stick=W+N+S+E)
rt.mainloop()

