n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=set(l)
v=[]
for i in s:
    if l.count(i)==k:
        v.append(i)
if(v==[]):
    print('-1')
else:
    print(*v)