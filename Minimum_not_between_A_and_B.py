n=int(input())
b=list(map(int,input().split()))
x,y=map(int,input().split())
z=[]
A=[]
c=0
for i in  b:
    if i>=x and i<=y:
        z.append(i)
    else:
        A.append(i)
        
if len(A)==0:
    print(-1)
else:
    print(min(A))
            