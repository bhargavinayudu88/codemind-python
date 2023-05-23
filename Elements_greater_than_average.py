n=int(input())
a=list(map(int,input().split()))
b=sum(a)
c=b//n
s=0
for i in range(n):
    if a[i]>=c:
        s=s+1
print(s)

