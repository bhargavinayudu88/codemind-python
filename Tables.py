N,R=map(int,input().split())
for i in range(1,R+1):
    if i%2!=0:
        print(N,'x',i,'=',N*i)