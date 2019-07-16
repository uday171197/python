import numpy as np
import operator
l=[]
d=[]

def aircraft( maxtravel , farword ,reverse):
    c=0
    for i in range(len(farword)):
        for j in range(len(reverse)):
            if (farword[i][1]+reverse[j][1]==maxtravel):
                d.append([[i+1 ,j+1]])
                c=1
            elif(farword[i][1]+reverse[j][1]< maxtravel):
                l.append([[farword[i][1]+reverse[j][1]],[[i+1,j+1]]])
            
    if(c==1):
        print(d)
    else:
        sorted(l)
        print(l[-1][1])

maxtravel=int(input("maximum distance "))
print("enter the unique id and farward distace ",end='\n')
farword ,reverse =[],[]
for i in range(3):
    y=int(input())
    farword.append([i,y])
print("enter the unique id with reverse distance")
for i in range(1):
    y=int(input())
    reverse.append([i,y])
aircraft( maxtravel ,farword ,reverse)