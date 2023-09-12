n=input()
v=[]
b=[]
k=n.split(" ")
for i in k:
    v.append(i)
    for j in v:
        x=len(j)
        b.append(x)
print(max(b))
    
    