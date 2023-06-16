n=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if i%2==0:
        c=c+1
if c==n:
    print(True)
else:
    print(False)