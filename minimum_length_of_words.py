s=input()
v=[]
b=[]
k=s.split(" ")
for i in k:
    v.append(i)
    for j in v:
        l=len(j)
        b.append(l)
print(min(b))