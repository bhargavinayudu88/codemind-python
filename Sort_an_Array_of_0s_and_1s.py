n=int(input())
l=map(int,input().split())
v=[]
s=[]
for i in  l:
    if i==0:
        v.append(i)
    elif i==1:
        s.append(i)
print(*v,*s)
        