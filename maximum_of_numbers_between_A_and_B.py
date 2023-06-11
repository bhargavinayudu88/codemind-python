n=int(input())
b=list(map(int,input().split()))
x,y=map(int,input().split())
z=[]
c=0
for i in  b:
    if i>=x and i<=y:
        z.append(i)
if len(z)==0:
    print(-1)
else:
    print(max(z))
            