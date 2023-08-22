n=3
a=list(map(int,input().split()))
b=list(map(int,input().split()))
alice=0
bob=0
for i in range(n):
    if(a[i]>b[i]):
        alice+=1
    elif(b[i]>a[i]):
        bob+=1
    else:
        continue
print(alice,bob)
        