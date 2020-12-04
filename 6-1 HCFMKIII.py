a,b,=map(int, input().split())
ans=1
if a<=b:
    ed=a
else:
    ed=b
for i in range(1,ed+1):
    if a%i==b%i==0:
        ans=i
print(ans)
