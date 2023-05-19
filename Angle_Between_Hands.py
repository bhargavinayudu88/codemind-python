hh,mm=map(int,input().split(":"))
angle=((30*hh)-((11/2)*mm))
if angle<0:
    angle=angle*-1
t=angle
k=abs(t-360)
if t<k:
    print(t)
else:
    print(k)
