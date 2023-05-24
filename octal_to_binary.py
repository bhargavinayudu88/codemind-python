a=int(input())
s=0
i=0
g=[]
while(a):
    d=a%10
    s+=d*pow(8,i)
    i+=1
    a//=10
while(s!=0):
    d=s%2
    g.append(d)
    s//=2
g=g[::-1]
for i in g:
    print(i,end='')