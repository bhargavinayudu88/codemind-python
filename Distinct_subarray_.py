a=int(input())
b=int(input())
c=0
arr=[]
for i in range(a,b+1):
    arr.append(i)
for i in range(len(arr)):
    s=0
    for j in range(i,len(arr)):
        s+=arr[j]
        if(s%2!=0):
            c+=1;
print(c)
           