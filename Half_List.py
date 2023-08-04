n=int(input())
l=list(map(int,input().split()))
a=n//2
for i in range(n-1,a-1,-1):
    print(l[i],end=' ')
for i in range(0,a,1):
    print(l[i],end=' ')