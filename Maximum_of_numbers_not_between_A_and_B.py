n=int(input())
b=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
for i in b:
    if i<x or i>y:
        c.append(i)
if len(c)==0:
    print('-1')
else:
    print(max(c))