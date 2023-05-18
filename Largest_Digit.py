
n=int(input())
b=[]
while n>0:
    r=n%10
    b.append(r)
    n=n//10
print(max(b))

