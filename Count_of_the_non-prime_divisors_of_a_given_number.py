def prime(i):
    if i==1:
        return 0
    for j in range(2,int(i**0.5)+1):
        if  i%j==0:
            return 0
    else:
        return 1
x=int(input())
l=[]
m=[]
for i in range(1,x+1):
    if x%i==0:
        if prime(i):
            l.append(i)
        else:
            m.append(i)
print(len(m))
        