a=int(input())
b=int(input())
c=int(input())
x=0
y=0
z=0
if a>=b:
    if a>=c:
        x=a
        y=b
        z=c
    else:
        x=c
        y=a
        z=b
elif b>=c:
    x=b
    y=c
    z=a
else:
    x=c
    y=a
    z=b
if y+z<=x:
    print("無法構成三角形")
elif y**2+z**2<x**2:
    print("可構成三角形，且為銳角三角形")
elif y**2+z**2==x**2:
    print("可構成三角形，且為直角三角形")
elif y**2+z**2>x**2:
    print("可構成三角形，且為鈍角三角形")
