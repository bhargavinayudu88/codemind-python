n=int(input())
ans=0
for i in range(n):
    t=input()
    if(t=='X++'):
        ans+=1
    if(t=='++X'):
        ans+=1
    if(t=='X--'):
        ans-=1
    if(t=='--X'):
        ans-=1
print(ans)
    