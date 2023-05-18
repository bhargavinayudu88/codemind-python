n=int(input())
x=n
flag=0
t=10
sq=n**2
while n>0:
    r=sq%t
    if r==x:
        flag=1
        break
    n=n//10
    t=t*10
if flag==1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
        
        