n=int(input())
b=list(map(int,input().split()))
c=0
a=[]
for i in b:
    if i%2==0 and i not in a:
        a.append(i)
        c=c+1
    
print(c)