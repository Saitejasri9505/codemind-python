n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n,2):
    if(i%2==0):
        s=s+l[i]
print(s)