n=int(input())
sq=n*n
a1=0
a2=0
while n>0:
    r=n%10
    a1=a1*10+r
    n=n//10
s1=a1*a1
while s1>0:
        w=s1%10
        a2=a2*10+w
        s1=s1//10
if sq==a2:
    print(True)
else:
    print(False)