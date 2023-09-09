t=int(input())
for i in range(1,t+1):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    v=[]
    for i in a:
        v.append(i)
    for i in b:
        v.append(i)
    v.sort()
    for i in v:
        if(i!=max(v)):
            print(i,end=" ")
    print(max(v))
        
    