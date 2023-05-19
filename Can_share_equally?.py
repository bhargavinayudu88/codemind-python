a,b=map(int,input().split())
s=a*1
s1=b*2
if(b%2!=0 and a==0):
    print("NO")
else:
    if((s+s1)%2==0):
        print("YES")
    else:
        print("NO")
        
        
