t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    k=0
    for i in s:
        if s.count(i)==1:
            k=i
            break
    if(k==0):
        print("-1")
    else:
        print(k)
        
    