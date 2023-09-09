n=int(input())
l=list(map(int,input().split()))
a=max(l)
m=len(str(a))
c=0
for i in range(n):
    if len(str(l[i]))==m:
        c+=1
print(c)
    
    