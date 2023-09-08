n=int(input())
m=list(map(int,input().split()))
i=0
j=1
gcd=m[0]
while(j<n):
    if(m[j]%gcd==0):
        j+=1
    else:
        gcd=m[j]%gcd
        i+=1
print(gcd)
    
    