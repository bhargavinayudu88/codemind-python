s=input()
c=0
x=0
a=[]
for i in s:
    if (i in 'aeiou'):
        c=c+1
    else:
        if(c>x):
            x=c
            c=0
print(x)
