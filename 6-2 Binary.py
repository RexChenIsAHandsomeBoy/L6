x=int(input())
y=1
ans=[0]
while y>0:
    ans.append(x%2)
    y=x//2
for i in range(len(ans)-1,-1,-1):
    print(ans[i],end="")
