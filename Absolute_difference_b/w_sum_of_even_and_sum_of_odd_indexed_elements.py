n=int(input())
l=list(map(int,input().split()))
s=0
f=0
for i in range(0,n,2):
        s=s+l[i]
for i in range(1,n,2):      
        f=f+l[i]
print(abs(f-s))